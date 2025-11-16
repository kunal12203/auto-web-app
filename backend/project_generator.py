"""
Project Generator - Creates complete project structures
Supports: Simple HTML, React+Vite, Full-stack with payments
"""

import json
from typing import Dict, List, Optional
from payment_templates import PAYMENT_GATEWAYS

class ProjectGenerator:
    """Generate complete project structures"""

    @staticmethod
    def detect_project_type(prompt: str, needs_payment: bool) -> str:
        """Detect project type from prompt"""
        prompt_lower = prompt.lower()

        # Full-stack indicators
        if needs_payment or any(word in prompt_lower for word in [
            'backend', 'api', 'database', 'auth', 'login',
            'dashboard', 'admin', 'saas', 'platform'
        ]):
            return "fullstack"

        # React indicators
        if any(word in prompt_lower for word in [
            'react', 'spa', 'single page', 'interactive',
            'dynamic', 'app', 'application'
        ]):
            return "react"

        # Default to simple
        return "simple"

    @staticmethod
    def generate_simple_project(html_content: str, project_name: str) -> Dict[str, str]:
        """Generate simple HTML/CSS/JS project"""
        # Extract CSS from HTML
        css_start = html_content.find('<style>')
        css_end = html_content.find('</style>') + 8
        css_content = ""
        if css_start != -1:
            css_content = html_content[css_start + 7:css_end - 8]
            html_content = html_content[:css_start] + '<link rel="stylesheet" href="styles.css">' + html_content[css_end:]

        # Extract JS from HTML
        js_start = html_content.find('<script>')
        js_end = html_content.find('</script>') + 9
        js_content = ""
        if js_start != -1:
            js_content = html_content[js_start + 8:js_end - 9]
            html_content = html_content[:js_start] + '<script src="script.js"></script>' + html_content[js_end:]

        return {
            "index.html": html_content,
            "styles.css": css_content,
            "script.js": js_content,
            "README.md": ProjectGenerator._generate_readme(project_name, "simple"),
            ".gitignore": ProjectGenerator._generate_gitignore("simple"),
            "package.json": json.dumps({
                "name": project_name,
                "version": "1.0.0",
                "description": "Simple HTML website",
                "scripts": {
                    "start": "python -m http.server 8000",
                    "dev": "python -m http.server 8000"
                }
            }, indent=2)
        }

    @staticmethod
    def generate_react_project(prompt: str, project_name: str) -> Dict[str, str]:
        """Generate React + Vite project structure"""
        files = {}

        # package.json
        files["package.json"] = json.dumps({
            "name": project_name,
            "private": True,
            "version": "0.0.0",
            "type": "module",
            "scripts": {
                "dev": "vite",
                "build": "vite build",
                "preview": "vite preview"
            },
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0"
            },
            "devDependencies": {
                "@types/react": "^18.2.43",
                "@types/react-dom": "^18.2.17",
                "@vitejs/plugin-react": "^4.2.1",
                "vite": "^5.0.8"
            }
        }, indent=2)

        # vite.config.js
        files["vite.config.js"] = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000
  }
})
"""

        # index.html
        files["index.html"] = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>""" + project_name + """</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
"""

        # src/main.jsx
        files["src/main.jsx"] = """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
"""

        # src/App.jsx (will be filled by AI)
        files["src/App.jsx"] = """import { useState } from 'react'
import './App.css'

function App() {
  return (
    <div className="App">
      <h1>Welcome to """ + project_name + """</h1>
      {/* AI will generate content here */}
    </div>
  )
}

export default App
"""

        # src/index.css
        files["src/index.css"] = """* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}
"""

        # src/App.css (will be filled by AI)
        files["src/App.css"] = """/* App styles will be generated here */
"""

        # README.md
        files["README.md"] = ProjectGenerator._generate_readme(project_name, "react")

        # .gitignore
        files[".gitignore"] = ProjectGenerator._generate_gitignore("react")

        return files

    @staticmethod
    def generate_fullstack_project(
        prompt: str,
        project_name: str,
        payment_gateway: Optional[str] = None
    ) -> Dict[str, str]:
        """Generate full-stack React + FastAPI project"""
        files = {}

        # Root files
        files["README.md"] = ProjectGenerator._generate_readme(project_name, "fullstack", payment_gateway)
        files[".gitignore"] = ProjectGenerator._generate_gitignore("fullstack")
        files[".env.example"] = ProjectGenerator._generate_env_example(payment_gateway)

        # Frontend files (React)
        frontend_files = ProjectGenerator.generate_react_project(prompt, project_name)
        for path, content in frontend_files.items():
            files[f"frontend/{path}"] = content

        # Add payment component if needed
        if payment_gateway and payment_gateway in PAYMENT_GATEWAYS:
            gateway = PAYMENT_GATEWAYS[payment_gateway]
            files[f"frontend/src/components/Payment.jsx"] = gateway["frontend_component"]

            # Update frontend package.json with payment dependencies
            frontend_pkg = json.loads(files["frontend/package.json"])
            for dep in gateway["dependencies"]["frontend"]:
                frontend_pkg["dependencies"][dep] = "latest"
            files["frontend/package.json"] = json.dumps(frontend_pkg, indent=2)

        # Backend files (Python/FastAPI)
        files["backend/main.py"] = ProjectGenerator._generate_backend_main(payment_gateway)
        files["backend/requirements.txt"] = ProjectGenerator._generate_requirements(payment_gateway)
        files["backend/.env.example"] = files[".env.example"]

        # Payment routes if needed
        if payment_gateway and payment_gateway in PAYMENT_GATEWAYS:
            gateway = PAYMENT_GATEWAYS[payment_gateway]
            files[f"backend/routes/payment.py"] = gateway["backend_route"]

        return files

    @staticmethod
    def _generate_backend_main(payment_gateway: Optional[str] = None) -> str:
        """Generate FastAPI main.py"""
        routes_import = ""
        routes_include = ""

        if payment_gateway:
            routes_import = f"\nfrom routes.payment import router as payment_router"
            routes_include = f'\napp.include_router(payment_router, prefix="/api/{payment_gateway}", tags=["{payment_gateway}"])'

        return f"""from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv{routes_import}

load_dotenv()

app = FastAPI(title="API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {{"message": "API is running"}}

@app.get("/health")
async def health():
    return {{"status": "healthy"}}{routes_include}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
"""

    @staticmethod
    def _generate_requirements(payment_gateway: Optional[str] = None) -> str:
        """Generate requirements.txt"""
        base_deps = [
            "fastapi==0.104.1",
            "uvicorn[standard]==0.24.0",
            "python-dotenv==1.0.0",
            "pydantic==2.5.0"
        ]

        if payment_gateway and payment_gateway in PAYMENT_GATEWAYS:
            gateway = PAYMENT_GATEWAYS[payment_gateway]
            base_deps.extend(gateway["dependencies"]["backend"])

        return "\n".join(base_deps)

    @staticmethod
    def _generate_env_example(payment_gateway: Optional[str] = None) -> str:
        """Generate .env.example"""
        env_vars = ["# Environment Variables"]

        if payment_gateway and payment_gateway in PAYMENT_GATEWAYS:
            gateway = PAYMENT_GATEWAYS[payment_gateway]
            env_vars.append(f"\n# {gateway['name']} Configuration")
            for var in gateway["env_vars"]:
                env_vars.append(f"{var}=your_{var.lower()}_here")

        return "\n".join(env_vars)

    @staticmethod
    def _generate_readme(project_name: str, project_type: str, payment_gateway: Optional[str] = None) -> str:
        """Generate README.md"""
        readme = f"""# {project_name}

Generated by AI Website Builder

## Project Type: {project_type.upper()}

"""

        if project_type == "simple":
            readme += """## Getting Started

### Local Development
```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx http-server
```

Then open http://localhost:8000

### Using Docker
```bash
docker build -t """ + project_name + """ .
docker run -p 8080:80 """ + project_name + """
```

Then open http://localhost:8080
"""

        elif project_type == "react":
            readme += """## Getting Started

### Prerequisites
- Node.js 18+
- npm or yarn

### Installation
```bash
npm install
```

### Development
```bash
npm run dev
```

Then open http://localhost:3000

### Build for Production
```bash
npm run build
```

### Using Docker
```bash
docker build -t """ + project_name + """ .
docker run -p 3000:3000 """ + project_name + """
```
"""

        elif project_type == "fullstack":
            readme += """## Getting Started

### Prerequisites
- Node.js 18+
- Python 3.9+
- Docker (optional)

### Setup

1. **Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials
python main.py
```

2. **Frontend Setup**
```bash
cd frontend
npm install
npm run dev
```

### Using Docker Compose
```bash
docker-compose up --build
```

Frontend: http://localhost:3000
Backend API: http://localhost:8000
"""

            if payment_gateway:
                readme += f"""
### Payment Gateway: {payment_gateway.upper()}

This project includes {payment_gateway} integration. Make sure to:
1. Set up your {payment_gateway} account
2. Add API keys to `.env` file
3. Test in sandbox/test mode first
"""

        readme += """
## Project Structure

```
"""
        if project_type == "simple":
            readme += """.
├── index.html       # Main HTML file
├── styles.css       # Styles
├── script.js        # JavaScript
├── Dockerfile       # Docker configuration
└── README.md        # This file
"""
        elif project_type == "react":
            readme += """.
├── src/
│   ├── App.jsx      # Main component
│   ├── main.jsx     # Entry point
│   ├── index.css    # Global styles
│   └── App.css      # Component styles
├── public/          # Static assets
├── index.html       # HTML template
├── vite.config.js   # Vite configuration
├── package.json     # Dependencies
├── Dockerfile       # Docker configuration
└── README.md        # This file
"""
        else:
            readme += """.
├── frontend/        # React frontend
│   ├── src/
│   ├── public/
│   └── package.json
├── backend/         # FastAPI backend
│   ├── routes/
│   ├── main.py
│   └── requirements.txt
├── docker-compose.yml
├── .env.example
└── README.md
"""

        readme += """```

## Deployment

### Vercel (Frontend)
```bash
cd frontend
npm install -g vercel
vercel
```

### Docker (Full Stack)
```bash
docker-compose up -d
```

---

Built with ❤️ using AI Website Builder
"""

        return readme

    @staticmethod
    def _generate_gitignore(project_type: str) -> str:
        """Generate .gitignore"""
        gitignore = """# Dependencies
node_modules/
venv/
__pycache__/
*.pyc

# Environment variables
.env
.env.local

# Build outputs
dist/
build/
*.log

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
"""

        if project_type in ["react", "fullstack"]:
            gitignore += """
# Vite
dist-ssr/
*.local

# Testing
coverage/
"""

        return gitignore
