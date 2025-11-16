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
        system_message = """You are an expert web developer. Generate complete, beautiful, and functional HTML code based on user prompts.
The HTML should be self-contained with inline CSS and JavaScript.
Include modern styling with CSS3 and make it responsive.
Return ONLY the HTML code without any markdown formatting or explanations.
Make sure the code is production-ready and visually appealing."""

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"Create a website: {prompt}"}
            ],
            temperature=0.7,
            max_tokens=2000
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
