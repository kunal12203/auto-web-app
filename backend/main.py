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


def generate_website_code(prompt: str) -> str:
    """Generate website HTML/CSS/JS from a prompt using OpenAI GPT-4"""
    try:
        system_message = """You are an expert web developer specializing in modern, high-end website design. Generate complete, beautiful, and functional HTML code based on user prompts.

REQUIREMENTS:
1. The HTML should be self-contained with inline CSS and JavaScript
2. Use modern CSS3 features: gradients, animations, transitions, flexbox, grid
3. Make it fully responsive with mobile-first approach
4. Include smooth animations and micro-interactions
5. Use a modern color palette with gradients and proper contrast
6. Add proper navigation with anchor links or JavaScript-based routing
7. Include interactive elements with hover effects and transitions
8. Use modern typography with web-safe or Google Fonts
9. Add proper spacing, padding, and visual hierarchy
10. Make it production-ready and visually stunning

NAVIGATION:
- For single-page sites: Use smooth scrolling anchor links with proper navigation
- For multi-section sites: Implement JavaScript-based section navigation
- Always include a navigation menu with working links
- Use hash-based routing for multi-page functionality (e.g., #home, #about, #contact)
- Ensure all links and buttons are functional and interactive

DESIGN STYLE:
- Modern, clean, professional aesthetics
- Use glassmorphism, gradients, or neumorphism where appropriate
- Include subtle animations and transitions
- Proper use of whitespace and visual breathing room
- High contrast for accessibility
- Interactive hover states for all clickable elements

Return ONLY the complete HTML code without any markdown formatting or explanations.
The code should work immediately when loaded in a browser."""

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"Create a modern, high-end website: {prompt}"}
            ],
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

                if not prompt.strip():
                    await manager.send_message({
                        "type": "error",
                        "message": "Prompt cannot be empty"
                    }, websocket)
                    continue

                # Send acknowledgment
                await manager.send_message({
                    "type": "status",
                    "message": "Generating website..."
                }, websocket)

                # Generate website code
                html_code = generate_website_code(prompt)

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
