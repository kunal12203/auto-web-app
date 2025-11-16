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


def generate_html_with_claude(prompt: str) -> str:
    """Generate HTML content using Claude (for simple projects)"""
    system_prompt = """Expert web developer. Generate complete HTML with inline CSS/JS.

RESPONSIVE (CRITICAL):
- Mobile-first, viewport meta
- Breakpoints: <640px, 640-1024px, >1024px
- Flexbox/Grid, rem/em units
- Touch-friendly (44px min)

UI/UX:
- Modern CSS3: gradients, animations, glassmorphism
- Professional shadows, spacing (8px grid)
- Google Fonts, WCAG AA contrast

NAVIGATION:
- Hash navigation (href="#section")
- Smooth scrolling
- Mobile hamburger menu

INTERACTIVITY:
- Scroll animations
- Form validation
- Touch support

Return ONLY complete HTML, no markdown."""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=4096,
            messages=[{"role": "user", "content": f"{system_prompt}\n\nCreate: {prompt}"}]
        )

        html = response.content[0].text.strip()

        # Remove markdown code blocks
        if html.startswith("```html"):
            html = html[7:]
        elif html.startswith("```"):
            html = html[3:]
        if html.endswith("```"):
            html = html[:-3]

        return html.strip()

    except Exception as e:
        print(f"Error generating HTML: {str(e)}")
        return f"<!DOCTYPE html><html><body><h1>Error: {str(e)}</h1></body></html>"


def enhance_react_project_with_claude(files: Dict[str, str], prompt: str) -> Dict[str, str]:
    """Use Claude to generate React component code"""
    react_prompt = f"""Generate a React component for: {prompt}

Requirements:
- Modern React with hooks
- Responsive design
- Clean, maintainable code
- Inline styles or CSS modules

Return ONLY the App.jsx code, no markdown."""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=3000,
            messages=[{"role": "user", "content": react_prompt}]
        )

        app_jsx = response.content[0].text.strip()

        # Remove markdown
        if app_jsx.startswith("```jsx") or app_jsx.startswith("```javascript"):
            app_jsx = app_jsx.split("\n", 1)[1]
        if app_jsx.endswith("```"):
            app_jsx = app_jsx.rsplit("```", 1)[0]

        files["src/App.jsx"] = app_jsx.strip()

        # Generate corresponding CSS
        css_prompt = f"Generate CSS for this React app: {prompt}. Return ONLY CSS, no markdown."

        css_response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=2000,
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

    except Exception as e:
        print(f"Error enhancing React project: {str(e)}")

    return files


def enhance_fullstack_project_with_claude(
    files: Dict[str, str],
    prompt: str,
    payment_gateway: Optional[str]
) -> Dict[str, str]:
    """Use Claude to enhance fullstack project"""
    # Enhance React frontend
    frontend_files = {
        k.replace("frontend/", ""): v
        for k, v in files.items()
        if k.startswith("frontend/")
    }
    enhanced_frontend = enhance_react_project_with_claude(frontend_files, prompt)

    # Put back into files dict
    for k, v in enhanced_frontend.items():
        files[f"frontend/{k}"] = v

    # Generate API routes if needed (beyond payment)
    if "api" in prompt.lower() or "backend" in prompt.lower():
        api_prompt = f"""Generate FastAPI routes for: {prompt}

Return Python code for routes/api.py with:
- RESTful endpoints
- Pydantic models
- Error handling

Return ONLY Python code, no markdown."""

        try:
            response = client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=2000,
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

        except Exception as e:
            print(f"Error generating API routes: {str(e)}")

    return files


def update_specific_file(
    files: Dict[str, str],
    file_path: str,
    modification_prompt: str,
    current_content: str
) -> str:
    """Update a specific file using Claude"""
    update_prompt = f"""Modify this file: {file_path}

Current content:
```
{current_content[:2000]}
```

Change requested: {modification_prompt}

Return ONLY the complete updated file content, no markdown."""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=4096,
            messages=[{"role": "user", "content": update_prompt}]
        )

        updated_content = response.content[0].text.strip()

        # Remove markdown if present
        if "```" in updated_content:
            lines = updated_content.split("\n")
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines[-1].strip() == "```":
                lines = lines[:-1]
            updated_content = "\n".join(lines)

        return updated_content.strip()

    except Exception as e:
        print(f"Error updating file: {str(e)}")
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

                # Ask Claude to fix the error
                fix_prompt = f"""This file has a console error:

File: {file_path}
Error: {error}

Current content:
```
{all_files.get(file_path, '')[:2000]}
```

Fix the error and return the corrected file. Return ONLY code, no markdown."""

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
