"""
AI Website Builder Backend - Version 2
Production-ready project scaffolding with payment gateway support
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from anthropic import Anthropic
import os
from dotenv import load_dotenv
import json
from typing import Dict, List, Optional
import re

from project_generator import ProjectGenerator
from docker_generator import DockerGenerator
from payment_templates import PAYMENT_GATEWAYS, detect_payment_need
from templates import TEMPLATES, DEFAULT_VALUES

# Load environment variables
load_dotenv()

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Claude client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: dict, websocket: WebSocket):
        await websocket.send_json(message)

manager = ConnectionManager()


async def ask_user_choice(websocket: WebSocket, question: str, options: List[str]) -> str:
    """Ask user to choose from options via WebSocket"""
    await manager.send_message({
        "type": "question",
        "question": question,
        "options": options
    }, websocket)

    # Wait for user response
    data = await websocket.receive_text()
    response = json.loads(data)
    return response.get("answer", options[0])


def generate_project_files(
    prompt: str,
    project_name: str,
    project_type: str,
    payment_gateway: Optional[str] = None
) -> Dict[str, str]:
    """Generate complete project structure with all files"""

    # Generate base project files
    if project_type == "simple":
        # For simple projects, use Claude to generate HTML content first
        html_content = generate_html_with_claude(prompt)
        files = ProjectGenerator.generate_simple_project(html_content, project_name)
    elif project_type == "react":
        files = ProjectGenerator.generate_react_project(prompt, project_name)
        # Use Claude to generate React components
        files = enhance_react_project_with_claude(files, prompt)
    else:  # fullstack
        files = ProjectGenerator.generate_fullstack_project(prompt, project_name, payment_gateway)
        # Use Claude to generate both frontend and backend code
        files = enhance_fullstack_project_with_claude(files, prompt, payment_gateway)

    # Add Docker files
    docker_files = DockerGenerator.get_docker_files(project_type)
    files.update(docker_files)

    return files


def auto_select_template(user_prompt: str) -> str:
    """Automatically select best template - OPTIMIZED: ~50 tokens"""
    template_descriptions = "\n".join([
        f"{tid}: {t['name']} - {t['description']}"
        for tid, t in TEMPLATES.items()
    ])

    prompt = f"""Analyze & choose BEST template ID.

Templates:
{template_descriptions}

Request: {user_prompt}

Return ONLY template ID (e.g. "modern-landing"), nothing else."""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=50,
            messages=[{"role": "user", "content": prompt}]
        )

        template_id = response.content[0].text.strip().lower()
        if template_id in TEMPLATES:
            return template_id
        return "modern-landing"

    except Exception as e:
        print(f"Error selecting template: {str(e)}")
        return "modern-landing"


def extract_template_variables(template_html: str) -> list:
    """Extract all {{VARIABLE}} placeholders from template"""
    return list(set(re.findall(r'\{\{([A-Z_0-9]+)\}\}', template_html)))


def customize_template_with_ai(template_id: str, user_prompt: str) -> str:
    """Customize template - OPTIMIZED: ~150 tokens"""
    template = TEMPLATES.get(template_id)
    if not template:
        return None

    variables = extract_template_variables(template['html'])

    # ULTRA COMPRESSED PROMPT - ~150 tokens
    prompt = f"""Fill template vars from prompt. Return ONLY JSON.

Template: {template['name']}
Vars: {', '.join(variables)}

Rules:
- Use user colors or #667eea/#764ba2
- Extract titles, features, content
- Professional & concise
- Footer: "© 2024 All Rights Reserved"

User: {user_prompt}

JSON format: {{"VAR": "value"}}"""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.content[0].text.strip()

        # Parse JSON
        if result.startswith("```json"):
            result = result[7:]
        if result.startswith("```"):
            result = result[3:]
        if result.endswith("```"):
            result = result[:-3]

        variables_dict = json.loads(result.strip())

        # Fill defaults
        for var in variables:
            if var not in variables_dict:
                variables_dict[var] = DEFAULT_VALUES.get(var, f"[{var}]")

        # Replace in template
        customized_html = template['html']
        for var, value in variables_dict.items():
            customized_html = customized_html.replace(f"{{{{{var}}}}}", str(value))

        return customized_html

    except Exception as e:
        print(f"Error customizing template: {str(e)}")
        return None


def generate_html_with_claude(prompt: str) -> str:
    """Generate HTML - TOKEN OPTIMIZED: Uses templates first (200 tokens), fallback to from-scratch (4000 tokens)"""

    # STEP 1: Try template approach (200 tokens total)
    print("🎯 Token-optimized generation: Using template system...")
    template_id = auto_select_template(prompt)  # ~50 tokens
    print(f"✅ Selected template: {template_id}")

    customized_html = customize_template_with_ai(template_id, prompt)  # ~150 tokens

    if customized_html:
        print(f"✅ Template customized successfully! (~200 tokens used)")
        return customized_html

    # STEP 2: Fallback to from-scratch (only if template fails)
    print("⚠️ Template customization failed, falling back to from-scratch generation...")

    system_prompt = """Expert web dev. Generate complete HTML with inline CSS/JS.

RESPONSIVE: Mobile-first, viewport, breakpoints, flexbox/grid
UI/UX: Modern CSS3, gradients, animations, shadows, Google Fonts
NAVIGATION: Hash navigation only (href="#section"), sticky nav
INTERACTIVITY: Scroll animations, form validation
ACCESSIBILITY: Semantic HTML5, ARIA, keyboard nav

Return ONLY complete HTML, no markdown."""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=4096,
            messages=[{"role": "user", "content": f"{system_prompt}\n\nCreate: {prompt}"}]
        )

        html = response.content[0].text.strip()

        # Remove markdown
        if html.startswith("```html"):
            html = html[7:]
        elif html.startswith("```"):
            html = html[3:]
        if html.endswith("```"):
            html = html[:-3]

        print(f"✅ From-scratch generation complete (~4000 tokens used)")
        return html.strip()

    except Exception as e:
        print(f"❌ Error generating HTML: {str(e)}")
        return f"<!DOCTYPE html><html><body><h1>Error: {str(e)}</h1></body></html>"


def enhance_react_project_with_claude(files: Dict[str, str], prompt: str) -> Dict[str, str]:
    """Generate React component - TOKEN OPTIMIZED: Compressed prompts"""

    # COMPRESSED React prompt - ~400 tokens (vs 3000)
    react_prompt = f"""Generate React App.jsx for: {prompt}

Requirements:
- Modern hooks (useState, useEffect)
- Responsive (mobile-first)
- Clean, production code

Return App.jsx ONLY, no markdown."""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=2500,
            messages=[{"role": "user", "content": react_prompt}]
        )

        app_jsx = response.content[0].text.strip()

        # Clean markdown
        if app_jsx.startswith("```jsx") or app_jsx.startswith("```javascript"):
            app_jsx = app_jsx.split("\n", 1)[1]
        if app_jsx.endswith("```"):
            app_jsx = app_jsx.rsplit("```", 1)[0]

        files["src/App.jsx"] = app_jsx.strip()

        # COMPRESSED CSS prompt - ~100 tokens (vs 2000)
        css_prompt = f"CSS for: {prompt}. Modern, responsive. Return CSS only."

        css_response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1500,
            messages=[{"role": "user", "content": css_prompt}]
        )

        app_css = css_response.content[0].text.strip()
        if app_css.startswith("```css"):
            app_css = app_css[6:]
        elif app_css.startswith("```"):
            app_css = app_css[3:]
        if app_css.endswith("```"):
            app_css = app_css[:-3]

        files["src/App.css"] = app_css.strip()

        print(f"✅ React components generated (~500 tokens)")

    except Exception as e:
        print(f"❌ Error enhancing React project: {str(e)}")

    return files


def enhance_fullstack_project_with_claude(
    files: Dict[str, str],
    prompt: str,
    payment_gateway: Optional[str]
) -> Dict[str, str]:
    """Enhance fullstack - TOKEN OPTIMIZED"""
    # Enhance React frontend (already optimized)
    frontend_files = {
        k.replace("frontend/", ""): v
        for k, v in files.items()
        if k.startswith("frontend/")
    }
    enhanced_frontend = enhance_react_project_with_claude(frontend_files, prompt)

    # Put back
    for k, v in enhanced_frontend.items():
        files[f"frontend/{k}"] = v

    # Generate API routes if needed - COMPRESSED
    if "api" in prompt.lower() or "backend" in prompt.lower():
        # COMPRESSED prompt - ~200 tokens (vs 2000)
        api_prompt = f"""FastAPI routes for: {prompt}

Include:
- RESTful endpoints
- Pydantic models
- Error handling

Return routes/api.py code only, no markdown."""

        try:
            response = client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=1500,
                messages=[{"role": "user", "content": api_prompt}]
            )

            api_code = response.content[0].text.strip()
            if api_code.startswith("```python"):
                api_code = api_code[9:]
            elif api_code.startswith("```"):
                api_code = api_code[3:]
            if api_code.endswith("```"):
                api_code = api_code[:-3]

            files["backend/routes/api.py"] = api_code.strip()
            print(f"✅ API routes generated (~200 tokens)")

        except Exception as e:
            print(f"❌ Error generating API routes: {str(e)}")

    return files


def update_specific_file(
    files: Dict[str, str],
    file_path: str,
    modification_prompt: str,
    current_content: str
) -> str:
    """Update file - TOKEN OPTIMIZED: Compressed prompt"""

    # COMPRESSED update prompt - ~300 tokens (vs 2000+)
    update_prompt = f"""Modify: {file_path}

Current (first 1500 chars):
```
{current_content[:1500]}
```

Change: {modification_prompt}

Return complete updated file, no markdown."""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=4096,
            messages=[{"role": "user", "content": update_prompt}]
        )

        updated_content = response.content[0].text.strip()

        # Clean markdown
        if "```" in updated_content:
            lines = updated_content.split("\n")
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines[-1].strip() == "```":
                lines = lines[:-1]
            updated_content = "\n".join(lines)

        print(f"✅ File updated (~300 tokens)")
        return updated_content.strip()

    except Exception as e:
        print(f"❌ Error updating file: {str(e)}")
        return current_content


@app.get("/")
async def root():
    return {"message": "AI Website Builder API v2.0"}


@app.get("/health")
async def health():
    return {"status": "healthy", "version": "2.0"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)

            if message.get("type") == "generate":
                prompt = message.get("prompt", "")
                project_name = message.get("projectName", "my-website").lower().replace(" ", "-")

                if not prompt.strip():
                    await manager.send_message({
                        "type": "error",
                        "message": "Prompt cannot be empty"
                    }, websocket)
                    continue

                # Detect project needs
                await manager.send_message({
                    "type": "status",
                    "message": "Analyzing your requirements..."
                }, websocket)

                needs_payment = detect_payment_need(prompt)
                payment_gateway = None

                # Ask for payment gateway if needed
                if needs_payment:
                    gateway_choice = await ask_user_choice(
                        websocket,
                        "I detected you need payment processing. Which gateway would you like?",
                        ["stripe", "paypal", "razorpay", "none"]
                    )

                    if gateway_choice != "none":
                        payment_gateway = gateway_choice

                # Detect project type
                project_type = ProjectGenerator.detect_project_type(prompt, needs_payment)

                await manager.send_message({
                    "type": "status",
                    "message": f"Generating {project_type} project..."
                }, websocket)

                # Generate project files
                files = generate_project_files(prompt, project_name, project_type, payment_gateway)

                # Send project files to frontend
                await manager.send_message({
                    "type": "project",
                    "files": files,
                    "projectType": project_type,
                    "projectName": project_name,
                    "paymentGateway": payment_gateway
                }, websocket)

            elif message.get("type") == "update_file":
                # Update specific file
                file_path = message.get("filePath")
                current_content = message.get("currentContent")
                modification = message.get("modification")
                all_files = message.get("allFiles", {})

                await manager.send_message({
                    "type": "status",
                    "message": f"Updating {file_path}..."
                }, websocket)

                updated_content = update_specific_file(all_files, file_path, modification, current_content)

                await manager.send_message({
                    "type": "file_updated",
                    "filePath": file_path,
                    "content": updated_content
                }, websocket)

            elif message.get("type") == "console_error":
                # Handle console errors from frontend
                error = message.get("error")
                file_path = message.get("filePath", "unknown")
                all_files = message.get("allFiles", {})

                await manager.send_message({
                    "type": "status",
                    "message": f"Analyzing error in {file_path}..."
                }, websocket)

                # COMPRESSED error fix prompt - ~250 tokens (vs 2000+)
                fix_prompt = f"""Fix console error in {file_path}

Error: {error}

Code (first 1500 chars):
```
{all_files.get(file_path, '')[:1500]}
```

Return corrected file, no markdown."""

                try:
                    response = client.messages.create(
                        model="claude-sonnet-4-5",
                        max_tokens=4096,
                        messages=[{"role": "user", "content": fix_prompt}]
                    )

                    fixed_content = response.content[0].text.strip()

                    # Clean markdown
                    if "```" in fixed_content:
                        lines = fixed_content.split("\n")
                        if lines[0].startswith("```"):
                            lines = lines[1:]
                        if lines[-1].strip() == "```":
                            lines = lines[:-1]
                        fixed_content = "\n".join(lines)

                    print(f"✅ Console error fixed (~250 tokens)")

                    await manager.send_message({
                        "type": "file_updated",
                        "filePath": file_path,
                        "content": fixed_content.strip(),
                        "fixed": True
                    }, websocket)

                except Exception as e:
                    await manager.send_message({
                        "type": "error",
                        "message": f"Could not fix error: {str(e)}"
                    }, websocket)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as e:
        print(f"WebSocket error: {str(e)}")
        try:
            await manager.send_message({
                "type": "error",
                "message": str(e)
            }, websocket)
        except:
            pass
        manager.disconnect(websocket)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
