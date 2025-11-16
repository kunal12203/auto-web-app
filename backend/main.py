from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
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

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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


def extract_template_variables(template_html: str) -> list:
    """Extract all {{VARIABLE}} placeholders from template"""
    return list(set(re.findall(r'\{\{([A-Z_0-9]+)\}\}', template_html)))


def customize_template_with_ai(template_id: str, user_prompt: str) -> str:
    """Use AI to fill in template variables based on user prompt - COMPRESSED VERSION"""
    template = TEMPLATES.get(template_id)
    if not template:
        return None

    variables = extract_template_variables(template['html'])

    # COMPRESSED SYSTEM PROMPT - ~200 tokens instead of ~1200 tokens
    system_message = f"""Fill template variables with content from user prompt. Return ONLY valid JSON.

Template: {template['name']} - {template['description']}
Variables needed: {', '.join(variables)}

Rules:
1. Use user's colors or default to #667eea (primary), #764ba2 (secondary)
2. Extract titles, descriptions, features from prompt
3. Create professional, concise content for missing details
4. Keep values short and web-appropriate
5. Use "© 2024 All Rights Reserved" for FOOTER_TEXT if not specified

Return format: {{"VARIABLE_NAME": "value", ...}}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )

        result = response.choices[0].message.content.strip()

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
    """Generate website HTML/CSS/JS from a prompt using OpenAI GPT-4"""
    try:
        # If template is selected, use compressed template customization
        if template_id and not is_modification:
            customized_html = customize_template_with_ai(template_id, prompt)
            if customized_html:
                return customized_html
            # If template customization fails, fall back to regular generation

        system_message = """You are an expert web developer specializing in modern, high-end website design. Generate complete, beautiful, and functional HTML code based on user prompts.

CRITICAL RESPONSIVE DESIGN REQUIREMENTS:
1. Use mobile-first approach with proper viewport meta tag
2. Implement responsive breakpoints: mobile (< 640px), tablet (640px - 1024px), desktop (> 1024px)
3. Use CSS Grid and Flexbox for flexible layouts
4. Ensure all text is readable on all screen sizes (minimum 16px base font)
5. Make all interactive elements touch-friendly (minimum 44x44px)
6. Use relative units (rem, em, %, vw, vh) instead of fixed pixels where possible
7. Images must be responsive with max-width: 100% and height: auto
8. Test layouts work perfectly on mobile, tablet, and desktop

MODERN UI/UX REQUIREMENTS:
1. Self-contained HTML with inline CSS and JavaScript
2. Modern CSS3: gradients, animations, transitions, backdrop-filter, transforms
3. Smooth scroll behavior and scroll-triggered animations
4. Loading states and micro-interactions
5. Modern color palettes with proper contrast (WCAG AA minimum)
6. Contemporary typography with proper hierarchy (use Google Fonts)
7. Consistent spacing system (8px base grid)
8. Professional shadows and depth
9. Glassmorphism, gradients, or soft neumorphism design patterns
10. CSS variables for theme consistency

NAVIGATION & MULTI-PAGE SUPPORT (CRITICAL - IFRAME SAFE):
- **ALWAYS use hash-based navigation ONLY** (href="#home", href="#about", href="#contact")
- **NEVER use target="_blank", target="_top", target="_parent", or target="_self"**
- **NEVER use absolute URLs or external links in navigation**
- For single-page: Smooth scrolling anchor links with active state indicators
- For multi-page sites: Implement hash-based routing with JavaScript to show/hide sections
- Create sections with IDs matching hash routes (e.g., <section id="home">, <section id="about">)
- JavaScript router pattern:
  ```javascript
  // Hide all sections
  document.querySelectorAll('section').forEach(s => s.style.display = 'none');
  // Show active section based on hash
  const hash = window.location.hash || '#home';
  document.querySelector(hash)?.style.display = 'block';
  ```
- Update active menu items based on current hash
- Support browser back/forward navigation with hashchange event
- Include sticky/fixed navigation bar
- Mobile hamburger menu for responsive nav
- All buttons/links must use onClick with hash navigation or direct section showing

JAVASCRIPT INTERACTIVITY:
- Add smooth page transitions between sections
- Implement scroll animations (fade in, slide in)
- Create interactive components (accordions, tabs, modals, carousels)
- Add form validation and user feedback
- Include loading states and success messages
- Ensure all interactions work on touch devices

ACCESSIBILITY:
- Semantic HTML5 elements (header, nav, main, section, footer)
- Proper heading hierarchy (h1-h6)
- Alt text for images
- ARIA labels where needed
- Keyboard navigation support
- Focus indicators for interactive elements

CRITICAL IFRAME COMPATIBILITY REQUIREMENTS:
- **NEVER** include any of these attributes: target="_blank", target="_top", target="_parent"
- **ONLY** use hash-based navigation (href="#section-name")
- All navigation must stay within the same page using hash routing
- Links must not try to open new windows or navigate to external pages
- Use event.preventDefault() in JavaScript when handling navigation clicks
- Example correct navigation:
  ```html
  <a href="#home" onclick="showSection('home'); return false;">Home</a>
  <a href="#about" onclick="showSection('about'); return false;">About</a>
  ```

Return ONLY the complete, production-ready HTML code without markdown formatting or explanations.
The code must work perfectly when loaded directly in a browser and within an iframe."""

        messages = [{"role": "system", "content": system_message}]

        # Add conversation history for modifications
        if is_modification and conversation_history:
            messages.append({"role": "assistant", "content": f"Previous website code:\n\n{conversation_history[-1].get('html', '')}"})
            messages.append({"role": "user", "content": f"Modify the website with this change: {prompt}\n\nIMPORTANT: Return the COMPLETE updated HTML code, not just the changes."})
        else:
            messages.append({"role": "user", "content": f"Create a modern, high-end, fully responsive website: {prompt}"})

        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7,
            max_tokens=4000
        )

        generated_code = response.choices[0].message.content.strip()

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
