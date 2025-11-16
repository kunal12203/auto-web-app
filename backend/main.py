from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os
from dotenv import load_dotenv
import json
from typing import Dict, List

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


def generate_website_code(prompt: str, conversation_history: list = None, is_modification: bool = False) -> str:
    """Generate website HTML/CSS/JS from a prompt using OpenAI GPT-4"""
    try:
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

NAVIGATION & MULTI-PAGE SUPPORT:
- For single-page: Smooth scrolling anchor links with active state indicators
- For multi-page sites: Implement hash-based routing (#home, #about, #contact, etc.)
- Create JavaScript router to show/hide sections based on hash
- Maintain navigation state and update active menu items
- Support browser back/forward navigation
- Include sticky/fixed navigation bar
- Mobile hamburger menu for responsive nav

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

Return ONLY the complete, production-ready HTML code without markdown formatting or explanations.
The code must work perfectly when loaded directly in a browser."""

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

                if not prompt.strip():
                    await manager.send_message({
                        "type": "error",
                        "message": "Prompt cannot be empty"
                    }, websocket)
                    continue

                # Send acknowledgment
                status_msg = "Applying changes..." if is_modification else "Generating website..."
                await manager.send_message({
                    "type": "status",
                    "message": status_msg
                }, websocket)

                # Generate website code with conversation context
                html_code = generate_website_code(prompt, conversation_history, is_modification)

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
