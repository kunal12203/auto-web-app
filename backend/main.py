from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from anthropic import Anthropic
import os
from dotenv import load_dotenv
import json
from typing import Dict, List
import re
from templates import TEMPLATES, DEFAULT_VALUES

# Load environment variables
load_dotenv()

app = FastAPI()

# CORS middleware for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Claude (Anthropic) client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Store active WebSocket connections
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


def auto_select_template(user_prompt: str) -> str:
    """Automatically select the best template based on user prompt using Claude"""
    template_descriptions = "\n".join([
        f"{tid}: {t['name']} - {t['description']}"
        for tid, t in TEMPLATES.items()
    ])

    prompt = f"""Analyze this website request and choose the BEST matching template ID.

Available templates:
{template_descriptions}

User request: {user_prompt}

Return ONLY the template ID (e.g., "modern-landing" or "portfolio"), nothing else."""

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=50,
            messages=[{"role": "user", "content": prompt}]
        )

        template_id = response.content[0].text.strip().lower()

        # Validate template exists
        if template_id in TEMPLATES:
            return template_id

        # Default fallback
        return "modern-landing"

    except Exception as e:
        print(f"Error selecting template: {str(e)}")
        return "modern-landing"


def extract_template_variables(template_html: str) -> list:
    """Extract all {{VARIABLE}} placeholders from template"""
    return list(set(re.findall(r'\{\{([A-Z_0-9]+)\}\}', template_html)))


def customize_template_with_ai(template_id: str, user_prompt: str) -> str:
    """Use Claude AI to fill in template variables - ULTRA COMPRESSED"""
    template = TEMPLATES.get(template_id)
    if not template:
        return None

    variables = extract_template_variables(template['html'])

    # ULTRA COMPRESSED PROMPT for Claude - ~150 tokens
    prompt = f"""Fill template vars with content from prompt. Return ONLY JSON.

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
            model="claude-3-5-sonnet-20240620",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.content[0].text.strip()

        # Parse JSON response
        if result.startswith("```json"):
            result = result[7:]
        if result.startswith("```"):
            result = result[3:]
        if result.endswith("```"):
            result = result[:-3]

        variables_dict = json.loads(result.strip())

        # Fill in defaults for missing variables
        for var in variables:
            if var not in variables_dict:
                variables_dict[var] = DEFAULT_VALUES.get(var, f"[{var}]")

        # Replace variables in template
        customized_html = template['html']
        for var, value in variables_dict.items():
            customized_html = customized_html.replace(f"{{{{{var}}}}}", str(value))

        return customized_html

    except Exception as e:
        print(f"Error customizing template: {str(e)}")
        return None


def generate_website_code(prompt: str, conversation_history: list = None, is_modification: bool = False, template_id: str = None) -> str:
    """Generate website HTML/CSS/JS using Claude API with automatic template selection"""
    try:
        # Auto-select template if not provided and not a modification
        if not template_id and not is_modification:
            template_id = auto_select_template(prompt)
            print(f"Auto-selected template: {template_id}")

        # Use template customization (ultra compressed)
        if template_id and not is_modification:
            customized_html = customize_template_with_ai(template_id, prompt)
            if customized_html:
                return customized_html
            # If template customization fails, fall back to regular generation

        # COMPRESSED SYSTEM PROMPT for Claude - from scratch generation fallback
        system_prompt = """Expert web dev. Generate complete HTML with inline CSS/JS.

RESPONSIVE (CRITICAL):
- Mobile-first, viewport meta
- Breakpoints: <640px, 640-1024px, >1024px
- Flexbox/Grid, rem/em units
- Touch-friendly (44px min)

UI/UX:
- Modern CSS3: gradients, animations, glassmorphism
- Professional shadows, spacing (8px grid)
- Google Fonts, WCAG AA contrast

NAVIGATION (IFRAME-SAFE):
- ONLY hash navigation (href="#home")
- NEVER target="_blank/_top/_parent"
- Hash routing for multi-page
- Sticky nav, mobile hamburger

INTERACTIVITY:
- Scroll animations
- Form validation
- Touch support

ACCESSIBILITY:
- Semantic HTML5
- Proper headings, ARIA
- Keyboard nav

Return ONLY complete HTML, no markdown."""

        # Build user message for Claude
        if is_modification and conversation_history:
            user_message = f"""Previous website:
{conversation_history[-1].get('html', '')[:1000]}...

Modify with: {prompt}

Return COMPLETE updated HTML."""
        else:
            user_message = f"{system_prompt}\n\nCreate website: {prompt}"

        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=4096,
            messages=[{"role": "user", "content": user_message}]
        )

        generated_code = response.content[0].text.strip()

        # Remove markdown code blocks if present
        if generated_code.startswith("```html"):
            generated_code = generated_code[7:]
        elif generated_code.startswith("```"):
            generated_code = generated_code[3:]

        if generated_code.endswith("```"):
            generated_code = generated_code[:-3]

        return generated_code.strip()

    except Exception as e:
        error_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background: #f5f5f5;
                }}
                .error {{
                    background: #fff;
                    padding: 2rem;
                    border-radius: 8px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                    color: #d32f2f;
                }}
            </style>
        </head>
        <body>
            <div class="error">
                <h2>Error Generating Website</h2>
                <p>{str(e)}</p>
            </div>
        </body>
        </html>
        """
        return error_html


@app.get("/")
async def root():
    return {"message": "Website Builder API is running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Receive prompt from client
            data = await websocket.receive_text()
            message = json.loads(data)

            if message.get("type") == "generate":
                prompt = message.get("prompt", "")
                conversation_history = message.get("conversationHistory", [])
                is_modification = message.get("isModification", False)
                template_id = message.get("templateId", None)

                if not prompt.strip():
                    await manager.send_message({
                        "type": "error",
                        "message": "Prompt cannot be empty"
                    }, websocket)
                    continue

                # Send acknowledgment
                status_msg = "Applying changes..." if is_modification else ("Customizing template..." if template_id else "Generating website...")
                await manager.send_message({
                    "type": "status",
                    "message": status_msg
                }, websocket)

                # Generate website code with conversation context and template
                html_code = generate_website_code(prompt, conversation_history, is_modification, template_id)

                # Send generated code back to client
                await manager.send_message({
                    "type": "code",
                    "html": html_code,
                    "prompt": prompt
                }, websocket)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as e:
        print(f"WebSocket error: {str(e)}")
        manager.disconnect(websocket)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
