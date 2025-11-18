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
import logging
from datetime import datetime

from project_generator import ProjectGenerator
from docker_generator import DockerGenerator
from payment_templates import PAYMENT_GATEWAYS, detect_payment_need
from templates import TEMPLATES, DEFAULT_VALUES
from project_memory import project_memory
from project_runner import project_runner
from component_templates import detect_website_type, get_template_data

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

logger.info("=" * 80)
logger.info("🚀 AI Website Builder Backend Starting...")
logger.info("=" * 80)

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
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    logger.warning("⚠️ ANTHROPIC_API_KEY not found - AI generation will not work")
    client = None
else:
    logger.info("✅ Claude API key loaded")
    client = Anthropic(api_key=api_key)
    logger.info("✅ Anthropic client initialized")

# Connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        logger.info("✅ Connection Manager initialized")

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"🔌 WebSocket connected (Total: {len(self.active_connections)})")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        logger.info(f"🔌 WebSocket disconnected (Total: {len(self.active_connections)})")

    async def send_message(self, message: dict, websocket: WebSocket):
        try:
            await websocket.send_json(message)
            logger.debug(f"📤 Sent message: {message.get('type', 'unknown')}")
        except Exception as e:
            logger.error(f"❌ Error sending message: {str(e)}")
            raise

manager = ConnectionManager()


async def ask_user_choice(websocket: WebSocket, question: str, options: List[str]) -> str:
    """Ask user to choose from options via WebSocket"""
    logger.info(f"❓ Asking user: {question}")
    logger.debug(f"   Options: {options}")

    await manager.send_message({
        "type": "question",
        "question": question,
        "options": options
    }, websocket)

    # Wait for user response
    logger.debug("⏳ Waiting for user response...")
    data = await websocket.receive_text()
    response = json.loads(data)
    answer = response.get("answer", options[0])
    logger.info(f"✅ User selected: {answer}")
    return answer


def generate_project_files(
    prompt: str,
    project_name: str,
    project_type: str,
    payment_gateway: Optional[str] = None
) -> Dict[str, str]:
    """Generate complete project structure with all files"""
    logger.info("=" * 60)
    logger.info(f"🏗️  Generating {project_type.upper()} project: {project_name}")
    logger.info(f"   Payment Gateway: {payment_gateway or 'None'}")
    logger.info(f"   Prompt: {prompt[:100]}...")
    logger.info("=" * 60)

    try:
        # Generate base project files
        if project_type == "simple":
            logger.info("📄 Generating Simple HTML project...")
            # For simple projects, use Claude to generate HTML content first
            html_content = generate_html_with_claude(prompt)
            files = ProjectGenerator.generate_simple_project(html_content, project_name)
            logger.info(f"✅ Simple project generated ({len(files)} files)")

        elif project_type == "react":
            logger.info("⚛️  Generating React + Vite project...")
            files = ProjectGenerator.generate_react_project(prompt, project_name)
            logger.info(f"   Base React scaffolding created ({len(files)} files)")
            # Use Claude to generate React components
            files = enhance_react_project_with_claude(files, prompt)
            logger.info(f"✅ React project enhanced ({len(files)} files)")

        else:  # fullstack
            logger.info("🚀 Generating Full-Stack project...")
            files = ProjectGenerator.generate_fullstack_project(prompt, project_name, payment_gateway)
            logger.info(f"   Base full-stack scaffolding created ({len(files)} files)")
            # Use Claude to generate both frontend and backend code
            files = enhance_fullstack_project_with_claude(files, prompt, payment_gateway)
            logger.info(f"✅ Full-stack project enhanced ({len(files)} files)")

        # Add Docker files
        logger.info("🐳 Adding Docker configuration...")
        docker_files = DockerGenerator.get_docker_files(project_type)
        files.update(docker_files)
        logger.info(f"✅ Docker files added ({len(docker_files)} files)")

        logger.info(f"🎉 Project generation complete! Total files: {len(files)}")
        return files

    except Exception as e:
        logger.error(f"❌ Error generating project: {str(e)}", exc_info=True)
        raise


def auto_select_template(user_prompt: str) -> str:
    """Automatically select best template - OPTIMIZED: ~50 tokens"""
    logger.info("🎯 Auto-selecting best template...")
    logger.debug(f"   Available templates: {list(TEMPLATES.keys())}")

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
        logger.debug("   Calling Claude API (~50 tokens)...")
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=50,
            messages=[{"role": "user", "content": prompt}]
        )

        template_id = response.content[0].text.strip().lower()
        logger.info(f"   Claude selected: {template_id}")

        if template_id in TEMPLATES:
            logger.info(f"✅ Template selected: {template_id}")
            return template_id

        logger.warning(f"⚠️  Invalid template '{template_id}', using default 'modern-landing'")
        return "modern-landing"

    except Exception as e:
        logger.error(f"❌ Error selecting template: {str(e)}", exc_info=True)
        logger.info("   Falling back to 'modern-landing'")
        return "modern-landing"


def extract_template_variables(template_html: str) -> list:
    """Extract all {{VARIABLE}} placeholders from template"""
    return list(set(re.findall(r'\{\{([A-Z_0-9]+)\}\}', template_html)))


def customize_template_with_ai(template_id: str, user_prompt: str) -> str:
    """Customize template - OPTIMIZED: ~150 tokens"""
    logger.info(f"✏️  Customizing template '{template_id}' with AI...")

    template = TEMPLATES.get(template_id)
    if not template:
        logger.error(f"❌ Template '{template_id}' not found!")
        return None

    variables = extract_template_variables(template['html'])
    logger.debug(f"   Found {len(variables)} variables: {variables}")

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
        logger.debug("   Calling Claude API (~150 tokens)...")
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.content[0].text.strip()
        logger.debug(f"   Received response ({len(result)} chars)")

        # Parse JSON
        if result.startswith("```json"):
            result = result[7:]
        if result.startswith("```"):
            result = result[3:]
        if result.endswith("```"):
            result = result[:-3]

        logger.debug("   Parsing JSON response...")
        variables_dict = json.loads(result.strip())
        logger.debug(f"   Parsed {len(variables_dict)} variables")

        # Fill defaults
        logger.debug("   Filling in default values for missing variables...")
        for var in variables:
            if var not in variables_dict:
                default_val = DEFAULT_VALUES.get(var, f"[{var}]")
                variables_dict[var] = default_val
                logger.debug(f"      {var} = {default_val} (default)")

        # Replace in template
        logger.debug("   Replacing variables in template...")
        customized_html = template['html']
        for var, value in variables_dict.items():
            customized_html = customized_html.replace(f"{{{{{var}}}}}", str(value))

        logger.info(f"✅ Template customized successfully! ({len(customized_html)} chars)")
        return customized_html

    except Exception as e:
        logger.error(f"❌ Error customizing template: {str(e)}", exc_info=True)
        return None


def verify_file_completeness(file_path: str, content: str, strict: bool = True) -> bool:
    """Verify that a generated file is complete and not truncated"""
    if not content or len(content.strip()) < 10:
        logger.warning(f"⚠️  {file_path} appears to be empty or too short ({len(content)} chars)")
        return False

    # Check for common truncation indicators (these are reliable)
    truncation_indicators = [
        "// ... rest of the code",
        "<!-- ... -->",
        "# ... rest of the file",
        "// ... (rest of"
    ]

    content_lower = content.lower()
    for indicator in truncation_indicators:
        if indicator.lower() in content_lower:
            logger.warning(f"⚠️  {file_path} may be truncated - found '{indicator}'")
            return False

    # For component files, be more lenient (they're small and self-contained)
    if 'components/' in file_path:
        # Just check for any export statement
        if 'export' not in content:
            logger.warning(f"⚠️  {file_path} missing export statement")
            return False
        # Check minimum length for a real component (>100 chars)
        if len(content.strip()) < 100:
            logger.warning(f"⚠️  {file_path} too short for a component")
            return False
        logger.debug(f"✅ {file_path} appears complete ({len(content)} chars)")
        return True

    # For main files (App.jsx, api.py), be more strict
    if strict and file_path.endswith(('.jsx', '.js', '.tsx', '.ts', '.py')):
        open_braces = content.count('{')
        close_braces = content.count('}')
        open_parens = content.count('(')
        close_parens = content.count(')')
        open_brackets = content.count('[')
        close_brackets = content.count(']')

        # Relaxed tolerance: JSX can have slight imbalances due to template strings
        if abs(open_braces - close_braces) > 5:
            logger.warning(f"⚠️  {file_path} has unbalanced braces: {open_braces} open, {close_braces} close")
            return False
        if abs(open_parens - close_parens) > 5:
            logger.warning(f"⚠️  {file_path} has unbalanced parentheses: {open_parens} open, {close_parens} close")
            return False
        if abs(open_brackets - close_brackets) > 5:
            logger.warning(f"⚠️  {file_path} has unbalanced brackets: {open_brackets} open, {close_brackets} close")
            return False

    # Check for incomplete JSX/React components (main App.jsx only)
    if strict and file_path.endswith(('.jsx', '.tsx')) and 'App.jsx' in file_path:
        if 'export default' not in content and 'export {' not in content:
            logger.warning(f"⚠️  {file_path} missing export statement - may be incomplete")
            return False

    logger.debug(f"✅ {file_path} appears complete ({len(content)} chars)")
    return True


def generate_html_with_claude(prompt: str) -> str:
    """Generate HTML - TOKEN OPTIMIZED: Uses templates first (200 tokens), fallback to from-scratch (4000 tokens)"""
    logger.info("🎨 Generating HTML with Claude...")

    # STEP 1: Try template approach (200 tokens total)
    logger.info("   STEP 1: Trying template-based generation (~200 tokens)...")
    template_id = auto_select_template(prompt)  # ~50 tokens

    customized_html = customize_template_with_ai(template_id, prompt)  # ~150 tokens

    if customized_html:
        logger.info("✅ Template-based generation successful! (~200 tokens used)")
        return customized_html

    # STEP 2: Fallback to from-scratch (only if template fails)
    logger.warning("⚠️  Template customization failed, falling back to from-scratch generation...")
    logger.info("   STEP 2: From-scratch generation (~4000 tokens)...")

    system_prompt = """Expert web dev. Generate complete HTML with inline CSS/JS.

RESPONSIVE: Mobile-first, viewport, breakpoints, flexbox/grid
UI/UX: Modern CSS3, gradients, animations, shadows, Google Fonts
NAVIGATION: Hash navigation only (href="#section"), sticky nav
INTERACTIVITY: Scroll animations, form validation
ACCESSIBILITY: Semantic HTML5, ARIA, keyboard nav

Return ONLY complete HTML, no markdown."""

    try:
        logger.debug("   Calling Claude API with from-scratch prompt...")
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=4096,
            messages=[{"role": "user", "content": f"{system_prompt}\n\nCreate: {prompt}"}]
        )

        html = response.content[0].text.strip()
        logger.debug(f"   Received HTML ({len(html)} chars)")

        # Remove markdown
        if html.startswith("```html"):
            html = html[7:]
        elif html.startswith("```"):
            html = html[3:]
        if html.endswith("```"):
            html = html[:-3]

        logger.info("✅ From-scratch generation complete (~4000 tokens used)")
        return html.strip()

    except Exception as e:
        logger.error(f"❌ Error generating HTML: {str(e)}", exc_info=True)
        return f"<!DOCTYPE html><html><body><h1>Error: {str(e)}</h1></body></html>"


def enhance_react_project_with_claude(files: Dict[str, str], prompt: str) -> Dict[str, str]:
    """Generate React components - STATIC TEMPLATES (0 tokens) or AI generation fallback"""

    logger.info("📦 Generating React components...")

    # STEP 0: Check if we can use static templates from disk (0 tokens!)
    website_type = detect_website_type(prompt)
    template_data = get_template_data(website_type) if website_type else {}

    if template_data:
        logger.info(f"   ✅ Using static templates for '{website_type}' website (0 tokens - loading from disk)")

        # Load complete templates from disk - NO AI NEEDED
        template_files = template_data.get("files", {})
        template_css = template_data.get("css", "")
        component_names = template_data.get("components", [])

        # Add all template components to files
        for component_name, component_code in template_files.items():
            files[f"src/components/{component_name}.jsx"] = component_code
            logger.info(f"      ✅ {component_name} loaded from template ({len(component_code)} chars)")

        # Generate App.jsx
        imports = "\n".join([f"import {name} from './components/{name}'" for name in component_names])
        components_jsx = "\n      ".join([f"<{name} />" for name in component_names])

        app_jsx = f"""import {{ useState }} from 'react'
import './App.css'
{imports}

function App() {{
  return (
    <div className="App">
      {components_jsx}
    </div>
  )
}}

export default App
"""
        files["src/App.jsx"] = app_jsx
        logger.info(f"   ✅ App.jsx generated with {len(component_names)} components")

        # Add CSS from template
        if template_css:
            files["src/App.css"] = template_css
            logger.info(f"   ✅ CSS loaded from template ({len(template_css)} chars)")

        logger.info(f"✅ Static template project generated: {len(component_names)} components (0 tokens used!)")
        return files

    # FALLBACK: AI Generation (only if no template match)
    logger.info("   No template match - using AI generation")

    # STEP 1: Identify components needed
    component_analysis_prompt = f"""Analyze this website request and identify the main React components needed.

Request: {prompt}

Return ONLY a JSON array of component names (no descriptions). Example:
["Header", "Hero", "Features", "Testimonials", "Footer"]

Max 6 components. Use PascalCase names."""

    try:
        logger.info("   Step 1: Analyzing required components...")
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=200,
            messages=[{"role": "user", "content": component_analysis_prompt}]
        )

        components_text = response.content[0].text.strip()
        # Clean markdown
        if components_text.startswith("```json"):
            components_text = components_text[7:]
        elif components_text.startswith("```"):
            components_text = components_text[3:]
        if components_text.endswith("```"):
            components_text = components_text[:-3]

        component_names = json.loads(components_text.strip())
        logger.info(f"   Found {len(component_names)} components: {', '.join(component_names)}")

        # STEP 2: Generate each component separately
        logger.info("   Step 2: Generating individual components with AI...")
        generated_components = []

        for component_name in component_names:
            logger.info(f"      Generating {component_name}...")

            # AI generation with retry
            max_retries = 2
            component_code = None

            for attempt in range(max_retries):
                tokens = 3000 if attempt == 0 else 4500
                retry_note = " (RETRY - must be COMPLETE)" if attempt > 0 else ""

                component_prompt = f"""Generate COMPLETE React component: {component_name}{retry_note}

Context: {prompt}

Requirements:
- Functional component with hooks (useState, useEffect as needed)
- Responsive design
- Modern styling with className
- MUST BE COMPLETE - no truncation, no cutoffs
- Include ALL necessary imports (React, useState, etc.)
- Export the component (export default or export const)

Return COMPLETE {component_name}.jsx code ONLY, no markdown.{' IMPORTANT: This is a retry because previous attempt was incomplete - generate the ENTIRE component.' if attempt > 0 else ''}"""

                try:
                    if attempt > 0:
                        logger.info(f"         Retry {attempt}/{max_retries - 1} with {tokens} tokens...")

                    comp_response = client.messages.create(
                        model="claude-sonnet-4-5",
                        max_tokens=tokens,
                        messages=[{"role": "user", "content": component_prompt}]
                    )

                    component_code = comp_response.content[0].text.strip()

                    # Clean markdown
                    if component_code.startswith("```jsx") or component_code.startswith("```javascript"):
                        component_code = component_code.split("\n", 1)[1]
                    if component_code.endswith("```"):
                        component_code = component_code.rsplit("```", 1)[0]

                    component_code = component_code.strip()

                    # Verify component is complete
                    if verify_file_completeness(f"src/components/{component_name}.jsx", component_code):
                        files[f"src/components/{component_name}.jsx"] = component_code
                        generated_components.append(component_name)
                        logger.info(f"      ✅ {component_name} complete ({len(component_code)} chars)")
                        break  # Success! Exit retry loop
                    else:
                        if attempt < max_retries - 1:
                            logger.warning(f"         Component incomplete, retrying...")
                        else:
                            logger.warning(f"      ⚠️  {component_name} incomplete after {max_retries} attempts, skipping")

                except Exception as e:
                    logger.error(f"         Error generating {component_name}: {e}")
                    if attempt >= max_retries - 1:
                        logger.warning(f"      ⚠️  {component_name} failed after {max_retries} attempts, skipping")

        # Use generated_components for the rest
        component_names = generated_components

        if len(component_names) == 0:
            logger.error("   ❌ No components were generated successfully!")
            raise Exception("Component generation failed - no valid components created")

        # STEP 3: Generate App.jsx
        logger.info("   Step 3: Generating App.jsx...")
        imports = "\n".join([f"import {name} from './components/{name}'" for name in component_names])
        components_jsx = "\n      ".join([f"<{name} />" for name in component_names])

        app_jsx = f"""import {{ useState }} from 'react'
import './App.css'
{imports}

function App() {{
  return (
    <div className="App">
      {components_jsx}
    </div>
  )
}}

export default App
"""
        files["src/App.jsx"] = app_jsx
        logger.info(f"   ✅ App.jsx generated with {len(component_names)} components")

        # STEP 4: Generate CSS
        logger.info("   Step 4: Generating styles...")
        css_max_retries = 2
        for css_attempt in range(css_max_retries):
            tokens = 4000 if css_attempt == 0 else 6000
            retry_note = " (RETRY - must be COMPLETE)" if css_attempt > 0 else ""

            css_prompt = f"""Generate COMPLETE CSS for: {prompt}{retry_note}

Components: {', '.join(component_names)}

Requirements:
- Modern, responsive design
- Mobile-first breakpoints (@media queries)
- Professional colors and typography
- Smooth animations and transitions
- Styles for ALL components listed above
- MUST BE COMPLETE - no truncation

Return COMPLETE CSS only, no markdown.{' IMPORTANT: Previous attempt was incomplete - generate ALL styles.' if css_attempt > 0 else ''}"""

            try:
                if css_attempt > 0:
                    logger.info(f"      CSS retry {css_attempt}/{css_max_retries - 1} with {tokens} tokens...")

                css_response = client.messages.create(
                    model="claude-sonnet-4-5",
                    max_tokens=tokens,
                    messages=[{"role": "user", "content": css_prompt}]
                )

                app_css = css_response.content[0].text.strip()
                if app_css.startswith("```css"):
                    app_css = app_css[6:]
                elif app_css.startswith("```"):
                    app_css = app_css[3:]
                if app_css.endswith("```"):
                    app_css = app_css[:-3]

                app_css = app_css.strip()

                if len(app_css) > 200:
                    files["src/App.css"] = app_css
                    logger.info(f"   ✅ CSS generated ({len(app_css)} chars)")
                    break
                else:
                    if css_attempt < css_max_retries - 1:
                        logger.warning(f"      CSS too short ({len(app_css)} chars), retrying...")
                    else:
                        logger.warning(f"   ⚠️  CSS generation incomplete, using minimal fallback")
                        files["src/App.css"] = "/* Add your styles here */\n* { margin: 0; padding: 0; box-sizing: border-box; }"

            except Exception as e:
                logger.error(f"      Error generating CSS: {e}")
                if css_attempt >= css_max_retries - 1:
                    files["src/App.css"] = "/* Add your styles here */\n* { margin: 0; padding: 0; box-sizing: border-box; }"

        logger.info(f"✅ AI-generated project: {len(component_names)} components")
        return files

    except Exception as e:
        logger.error(f"❌ Error in generation: {str(e)}")
        # Fallback to simple single-component approach
        logger.info("   Falling back to simple single-component approach...")
        simple_app = """import { useState } from 'react'
import './App.css'

function App() {
  return (
    <div className="App">
      <h1>Welcome</h1>
      <p>Component generation failed. Please regenerate.</p>
    </div>
  )
}

export default App
"""
        files["src/App.jsx"] = simple_app
        files["src/App.css"] = "* { margin: 0; padding: 0; box-sizing: border-box; }"
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
- MUST BE COMPLETE - no truncation or cutoffs

Return COMPLETE routes/api.py code only, no markdown."""

        try:
            response = client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=4000,
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

            # Verify API routes are complete
            if not verify_file_completeness("backend/routes/api.py", api_code):
                logger.error("❌ Generated API routes appear to be incomplete!")
                raise Exception("Generated API routes are incomplete or truncated")

            logger.info(f"✅ API routes generated and verified")

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
            logger.debug("📥 Waiting for message from client...")
            data = await websocket.receive_text()
            message = json.loads(data)
            message_type = message.get("type", "unknown")

            logger.info("=" * 60)
            logger.info(f"📨 Received message: {message_type}")
            logger.info("=" * 60)

            if message.get("type") == "generate":
                prompt = message.get("prompt", "")
                project_name = message.get("projectName", "my-website").lower().replace(" ", "-")
                existing_session_id = message.get("sessionId")  # Check if updating existing project
                existing_files = message.get("files", {})  # Get current files if updating

                # MULTI-TURN SUPPORT: Check if this is an update to existing project
                is_update = existing_session_id is not None and len(existing_files) > 0

                if is_update:
                    logger.info(f"💬 Multi-turn chat request (updating existing project):")
                    logger.info(f"   Session ID: {existing_session_id}")
                    logger.info(f"   Update prompt: {prompt[:200]}...")
                    logger.info(f"   Existing files: {len(existing_files)}")
                else:
                    logger.info(f"🎨 Generate request (new project):")
                    logger.info(f"   Project Name: {project_name}")
                    logger.info(f"   Prompt: {prompt[:200]}...")

                if not prompt.strip():
                    logger.warning("⚠️  Empty prompt received!")
                    await manager.send_message({
                        "type": "error",
                        "message": "Prompt cannot be empty"
                    }, websocket)
                    continue

                # HANDLE MULTI-TURN UPDATE
                if is_update:
                    logger.info("🔧 Processing as file update (not regenerating entire project)...")
                    await manager.send_message({
                        "type": "status",
                        "message": "Analyzing what needs to be updated..."
                    }, websocket)

                    # Smart update: identify which files to modify based on prompt
                    update_prompt = f"""Analyze this update request for an existing React project.

Current project has these files:
{', '.join(existing_files.keys())}

User request: {prompt}

Return ONLY a JSON object with:
{{"files_to_update": ["list", "of", "file", "paths"], "reason": "why these files"}}

Example: {{"files_to_update": ["src/components/Hero.jsx", "src/App.css"], "reason": "User wants to change hero section styling"}}"""

                    try:
                        update_analysis = client.messages.create(
                            model="claude-sonnet-4-5",
                            max_tokens=500,
                            messages=[{"role": "user", "content": update_prompt}]
                        )

                        analysis_text = update_analysis.content[0].text.strip()
                        if analysis_text.startswith("```json"):
                            analysis_text = analysis_text[7:]
                        elif analysis_text.startswith("```"):
                            analysis_text = analysis_text[3:]
                        if analysis_text.endswith("```"):
                            analysis_text = analysis_text[:-3]

                        update_plan = json.loads(analysis_text.strip())
                        files_to_update = update_plan.get("files_to_update", [])
                        update_reason = update_plan.get("reason", "Updating files")

                        logger.info(f"   Update plan: {update_reason}")
                        logger.info(f"   Files to modify: {', '.join(files_to_update)}")

                        await manager.send_message({
                            "type": "status",
                            "message": f"Updating {len(files_to_update)} files..."
                        }, websocket)

                        # Update only the identified files
                        updated_files = existing_files.copy()

                        for file_path in files_to_update:
                            if file_path not in existing_files:
                                logger.warning(f"   File {file_path} not found, skipping")
                                continue

                            logger.info(f"   Updating {file_path}...")

                            # Use existing update logic with memory context
                            context = project_memory.get_update_context(
                                session_id=existing_session_id,
                                file_to_update=file_path,
                                current_file_content=existing_files[file_path]
                            )

                            file_update_prompt = f"""{context}

USER REQUEST: {prompt}

Return complete updated file, no markdown."""

                            try:
                                update_response = client.messages.create(
                                    model="claude-sonnet-4-5",
                                    max_tokens=4096,
                                    messages=[{"role": "user", "content": file_update_prompt}]
                                )

                                updated_content = update_response.content[0].text.strip()

                                # Clean markdown
                                if "```" in updated_content:
                                    lines = updated_content.split("\n")
                                    if lines[0].startswith("```"):
                                        lines = lines[1:]
                                    if lines[-1].strip() == "```":
                                        lines = lines[:-1]
                                    updated_content = "\n".join(lines)

                                updated_files[file_path] = updated_content.strip()
                                logger.info(f"   ✅ {file_path} updated")

                            except Exception as e:
                                logger.error(f"   ❌ Error updating {file_path}: {e}")

                        # Re-deploy with updated files
                        logger.info(f"🚀 Re-deploying project with updates...")
                        deployment_result = await project_runner.deploy_project(
                            project_id=existing_session_id,
                            files=updated_files,
                            project_name=project_name
                        )

                        if deployment_result['success']:
                            logger.info(f"✅ Project re-deployed at: {deployment_result['url']}")
                            live_url = deployment_result['url']
                        else:
                            logger.warning(f"⚠️ Re-deployment failed: {deployment_result.get('error', 'Unknown error')}")
                            live_url = None

                        # Send updated files back to frontend
                        await manager.send_message({
                            "type": "project",
                            "files": updated_files,
                            "sessionId": existing_session_id,
                            "liveUrl": live_url,
                            "isUpdate": True
                        }, websocket)
                        logger.info("✅ Multi-turn update complete!")
                        continue  # Skip new project generation

                    except Exception as e:
                        logger.error(f"❌ Multi-turn update failed: {e}")
                        # Fall through to regenerate entire project
                        logger.info("   Falling back to full regeneration...")

                # HANDLE NEW PROJECT GENERATION
                # Detect project needs
                logger.info("🔍 Analyzing requirements...")
                await manager.send_message({
                    "type": "status",
                    "message": "Analyzing your requirements..."
                }, websocket)

                needs_payment = detect_payment_need(prompt)
                logger.info(f"   Payment needed: {needs_payment}")
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
                        logger.info(f"💳 Payment gateway selected: {payment_gateway}")

                # Detect project type
                project_type = ProjectGenerator.detect_project_type(prompt, needs_payment)
                logger.info(f"📦 Project type detected: {project_type}")

                await manager.send_message({
                    "type": "status",
                    "message": f"Generating {project_type} project..."
                }, websocket)

                # Generate project files
                files = generate_project_files(prompt, project_name, project_type, payment_gateway)

                # CREATE PROJECT MEMORY - Prevent hallucination on future updates
                logger.info("🧠 Creating project memory fingerprint...")
                memory_data = project_memory.create_project_fingerprint(
                    project_name=project_name,
                    project_type=project_type,
                    files=files,
                    payment_gateway=payment_gateway,
                    original_prompt=prompt
                )
                session_id = memory_data["session_id"]
                logger.info(f"✅ Project memory created: {session_id}")

                # DEPLOY PROJECT TO GET LIVE URL
                logger.info(f"🚀 Deploying project to live server...")
                await manager.send_message({
                    "type": "status",
                    "message": "Deploying project to live server..."
                }, websocket)

                deployment_result = await project_runner.deploy_project(
                    project_id=session_id,
                    files=files,
                    project_name=project_name
                )

                if deployment_result['success']:
                    logger.info(f"✅ Project deployed at: {deployment_result['url']}")
                    live_url = deployment_result['url']
                else:
                    logger.warning(f"⚠️ Deployment failed: {deployment_result.get('error', 'Unknown error')}")
                    live_url = None

                # Send project files to frontend (include session_id and live_url)
                logger.info(f"📤 Sending project to frontend ({len(files)} files)...")
                await manager.send_message({
                    "type": "project",
                    "files": files,
                    "projectType": project_type,
                    "projectName": project_name,
                    "paymentGateway": payment_gateway,
                    "sessionId": session_id,  # Frontend stores this for updates
                    "liveUrl": live_url  # Live deployment URL
                }, websocket)
                logger.info("✅ Project sent successfully!")

            elif message.get("type") == "update_file":
                # Update specific file WITH PROJECT MEMORY
                file_path = message.get("filePath")
                current_content = message.get("currentContent")
                modification = message.get("modification")
                all_files = message.get("allFiles", {})
                session_id = message.get("sessionId")  # Get session from frontend

                logger.info(f"✏️  Update file request:")
                logger.info(f"   File: {file_path}")
                logger.info(f"   Session ID: {session_id}")
                logger.info(f"   Modification: {modification[:100]}...")

                await manager.send_message({
                    "type": "status",
                    "message": f"Updating {file_path}..."
                }, websocket)

                # Use compressed context from memory (~200 tokens vs ~2000)
                logger.info("🧠 Retrieving memory context for update...")
                context = project_memory.get_update_context(
                    session_id=session_id,
                    file_to_update=file_path,
                    current_file_content=current_content
                )
                logger.debug(f"   Context size: {len(context)} chars")

                # MEMORY-AWARE UPDATE - prevents hallucination
                update_prompt = f"""{context}

USER REQUEST: {modification}

Return complete updated file, no markdown."""

                try:
                    logger.debug("   Calling Claude API for file update (~300 tokens)...")
                    response = client.messages.create(
                        model="claude-sonnet-4-5",
                        max_tokens=4096,
                        messages=[{"role": "user", "content": update_prompt}]
                    )
                    updated_content = response.content[0].text.strip()
                    logger.debug(f"   Received updated content ({len(updated_content)} chars)")

                    # Clean markdown
                    if "```" in updated_content:
                        lines = updated_content.split("\n")
                        if lines[0].startswith("```"):
                            lines = lines[1:]
                        if lines[-1].strip() == "```":
                            lines = lines[:-1]
                        updated_content = "\n".join(lines)

                    logger.info(f"✅ File updated with memory context (~300 tokens)")
                except Exception as e:
                    logger.error(f"❌ Error updating file: {str(e)}", exc_info=True)
                    updated_content = current_content

                logger.info("📤 Sending updated file to frontend...")
                await manager.send_message({
                    "type": "file_updated",
                    "filePath": file_path,
                    "content": updated_content
                }, websocket)
                logger.info("✅ Update sent successfully!")

            elif message.get("type") == "console_error":
                # Handle console errors WITH PROJECT MEMORY
                error = message.get("error")
                file_path = message.get("filePath", "unknown")
                all_files = message.get("allFiles", {})
                session_id = message.get("sessionId")  # Get session from frontend

                logger.info(f"🐛 Console error fix request:")
                logger.info(f"   File: {file_path}")
                logger.info(f"   Session ID: {session_id}")
                logger.info(f"   Error: {error if isinstance(error, str) else error.get('message', 'Unknown')}")

                await manager.send_message({
                    "type": "status",
                    "message": f"Analyzing error in {file_path}..."
                }, websocket)

                # Use compressed context from memory (~250 tokens vs ~2000)
                logger.info("🧠 Retrieving memory context for error fix...")
                context = project_memory.get_error_fix_context(
                    session_id=session_id,
                    error_info=error if isinstance(error, dict) else {"message": str(error)},
                    relevant_file=file_path,
                    file_content=all_files.get(file_path, '')
                )
                logger.debug(f"   Context size: {len(context)} chars")

                # MEMORY-AWARE ERROR FIX - prevents hallucination
                fix_prompt = f"""{context}

Return corrected file, no markdown."""

                try:
                    logger.debug("   Calling Claude API for error fix (~300 tokens)...")
                    response = client.messages.create(
                        model="claude-sonnet-4-5",
                        max_tokens=4096,
                        messages=[{"role": "user", "content": fix_prompt}]
                    )

                    fixed_content = response.content[0].text.strip()
                    logger.debug(f"   Received fixed content ({len(fixed_content)} chars)")

                    # Clean markdown
                    if "```" in fixed_content:
                        lines = fixed_content.split("\n")
                        if lines[0].startswith("```"):
                            lines = lines[1:]
                        if lines[-1].strip() == "```":
                            lines = lines[:-1]
                        fixed_content = "\n".join(lines)

                    logger.info(f"✅ Console error fixed with memory context (~300 tokens)")

                    logger.info("📤 Sending fixed file to frontend...")
                    await manager.send_message({
                        "type": "file_updated",
                        "filePath": file_path,
                        "content": fixed_content.strip(),
                        "fixed": True
                    }, websocket)
                    logger.info("✅ Fix sent successfully!")

                except Exception as e:
                    logger.error(f"❌ Error fixing console error: {str(e)}", exc_info=True)
                    await manager.send_message({
                        "type": "error",
                        "message": f"Could not fix error: {str(e)}"
                    }, websocket)

    except WebSocketDisconnect:
        logger.info("🔌 Client disconnected normally")
        manager.disconnect(websocket)
    except Exception as e:
        logger.error(f"❌ WebSocket error: {str(e)}", exc_info=True)
        try:
            await manager.send_message({
                "type": "error",
                "message": f"Server error: {str(e)}"
            }, websocket)
        except Exception as send_error:
            logger.error(f"❌ Could not send error message to client: {str(send_error)}")
        manager.disconnect(websocket)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
