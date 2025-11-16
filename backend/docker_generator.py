"""
Docker Configuration Generator
Generates Dockerfile and docker-compose.yml for different project types
"""

class DockerGenerator:
    """Generate Docker configurations"""

    @staticmethod
    def generate_simple_dockerfile() -> str:
        """Generate Dockerfile for simple HTML projects"""
        return """FROM nginx:alpine

# Copy website files
COPY index.html /usr/share/nginx/html/
COPY styles.css /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
"""

    @staticmethod
    def generate_react_dockerfile() -> str:
        """Generate multi-stage Dockerfile for React projects"""
        return """# Build stage
FROM node:18-alpine as build

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .

# Build the app
RUN npm run build

# Production stage
FROM nginx:alpine

# Copy built app from build stage
COPY --from=build /app/dist /usr/share/nginx/html

# Copy nginx configuration (optional)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
"""

    @staticmethod
    def generate_backend_dockerfile() -> str:
        """Generate Dockerfile for Python/FastAPI backend"""
        return """FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

    @staticmethod
    def generate_docker_compose(has_backend: bool = False, has_database: bool = False) -> str:
        """Generate docker-compose.yml"""
        compose = """version: '3.8'

services:
"""

        # Frontend service
        compose += """  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:80"
    environment:
      - NODE_ENV=production
"""

        if has_backend:
            compose += """    depends_on:
      - backend
"""

        # Backend service
        if has_backend:
            compose += """
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - ENVIRONMENT=production
    env_file:
      - .env
"""

            if has_database:
                compose += """    depends_on:
      - db
"""

        # Database service
        if has_database:
            compose += """
  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=app_db
      - POSTGRES_USER=app_user
      - POSTGRES_PASSWORD=app_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
"""

        return compose

    @staticmethod
    def generate_nginx_config() -> str:
        """Generate nginx configuration for React SPA"""
        return """server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;

    # Enable gzip compression
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types text/plain text/css text/xml text/javascript application/x-javascript application/xml+rss application/json;

    # Handle client-side routing
    location / {
        try_files $uri $uri/ /index.html;
    }

    # Cache static assets
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
}
"""

    @staticmethod
    def generate_dockerignore() -> str:
        """Generate .dockerignore"""
        return """node_modules
npm-debug.log
venv
__pycache__
*.pyc
.env
.git
.gitignore
README.md
.vscode
.idea
dist
build
coverage
"""

    @staticmethod
    def get_docker_files(project_type: str, has_database: bool = False) -> dict:
        """Get all Docker-related files for a project type"""
        files = {}

        if project_type == "simple":
            files["Dockerfile"] = DockerGenerator.generate_simple_dockerfile()
            files[".dockerignore"] = DockerGenerator.generate_dockerignore()

        elif project_type == "react":
            files["Dockerfile"] = DockerGenerator.generate_react_dockerfile()
            files[".dockerignore"] = DockerGenerator.generate_dockerignore()
            files["nginx.conf"] = DockerGenerator.generate_nginx_config()

        elif project_type == "fullstack":
            files["frontend/Dockerfile"] = DockerGenerator.generate_react_dockerfile()
            files["backend/Dockerfile"] = DockerGenerator.generate_backend_dockerfile()
            files["docker-compose.yml"] = DockerGenerator.generate_docker_compose(
                has_backend=True,
                has_database=has_database
            )
            files["frontend/.dockerignore"] = DockerGenerator.generate_dockerignore()
            files["backend/.dockerignore"] = DockerGenerator.generate_dockerignore()
            files["frontend/nginx.conf"] = DockerGenerator.generate_nginx_config()

        return files
