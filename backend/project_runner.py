"""
Project Runner Service
Deploys and runs generated projects on unique ports
"""

import os
import shutil
import subprocess
import json
import logging
import asyncio
from pathlib import Path
from typing import Dict, Optional, Tuple
import signal
import random

logger = logging.getLogger(__name__)

class ProjectRunner:
    def __init__(self, base_dir="/tmp/ai-website-builder-projects"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)

        # Track running projects: {project_id: {process, port, type, path}}
        self.running_projects: Dict[str, Dict] = {}

        # Port range for projects (3001-3100)
        self.port_range = range(3001, 3101)
        self.used_ports = set()

        logger.info(f"✅ Project Runner initialized at {self.base_dir}")

    def _get_available_port(self) -> int:
        """Get an available port from the range"""
        available_ports = [p for p in self.port_range if p not in self.used_ports]
        if not available_ports:
            # Try to find a truly available port
            import socket
            for port in self.port_range:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    if s.connect_ex(('localhost', port)) != 0:
                        return port
            raise Exception("No available ports in range")
        return random.choice(available_ports)

    def _detect_project_type(self, files: Dict[str, str]) -> str:
        """Detect the type of project from files"""
        # Check for full-stack project (backend + frontend folders)
        has_backend = any(f.startswith('backend/') for f in files.keys())
        has_frontend = any(f.startswith('frontend/') for f in files.keys())

        if has_backend and has_frontend:
            # Detect backend type
            backend_type = None
            if 'backend/requirements.txt' in files:
                backend_type = 'python'
            elif 'backend/package.json' in files:
                backend_type = 'nodejs'

            # Detect frontend type
            frontend_type = None
            if 'frontend/package.json' in files:
                pkg_json = files.get('frontend/package.json', '')
                if 'react' in pkg_json:
                    frontend_type = 'react'
                elif 'vue' in pkg_json:
                    frontend_type = 'vue'
                elif 'angular' in pkg_json:
                    frontend_type = 'angular'
                else:
                    frontend_type = 'nodejs'

            return f"fullstack-{backend_type}-{frontend_type}"

        # Single project type detection (existing logic)
        if 'package.json' in files:
            package_json = json.loads(files['package.json'])
            dependencies = package_json.get('dependencies', {})

            if 'react' in dependencies or 'react-dom' in dependencies:
                return 'react'
            elif 'vue' in dependencies:
                return 'vue'
            elif '@angular/core' in dependencies:
                return 'angular'
            elif 'next' in dependencies:
                return 'nextjs'
            elif 'express' in dependencies:
                return 'nodejs'
            else:
                return 'nodejs'

        # Check for Python project
        if 'requirements.txt' in files:
            return 'python'

        # Check for static HTML
        if any(f.endswith('.html') for f in files.keys()):
            return 'static'

        return 'unknown'

    def _create_env_file(self, project_path: Path, project_type: str):
        """Create necessary .env files for the project"""
        env_content = ""

        if project_type in ['react', 'vue', 'nextjs']:
            env_content = f"""# Auto-generated environment file
PORT=0
VITE_API_URL=http://localhost:8000
REACT_APP_API_URL=http://localhost:8000
"""
        elif project_type == 'nodejs':
            env_content = f"""# Auto-generated environment file
PORT=0
NODE_ENV=development
"""

        if env_content:
            env_file = project_path / '.env'
            env_file.write_text(env_content)
            logger.info(f"Created .env file for {project_type} project")

    def _write_files_to_disk(self, project_id: str, files: Dict[str, str]) -> Path:
        """Write project files to disk"""
        project_path = self.base_dir / project_id

        # Clean up if exists
        if project_path.exists():
            shutil.rmtree(project_path)

        project_path.mkdir(parents=True)

        # Write all files
        for file_path, content in files.items():
            full_path = project_path / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)

            # Write content
            full_path.write_text(content, encoding='utf-8')

        logger.info(f"✅ Wrote {len(files)} files to {project_path}")
        return project_path

    async def _run_static_server(self, project_path: Path, port: int) -> subprocess.Popen:
        """Run a static file server for HTML projects"""
        # Use Python's built-in HTTP server
        process = subprocess.Popen(
            ['python3', '-m', 'http.server', str(port)],
            cwd=str(project_path),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid
        )

        # Wait a bit for server to start
        await asyncio.sleep(2)

        logger.info(f"✅ Static server running on port {port}")
        return process

    async def _run_python_backend(self, project_path: Path, port: int) -> subprocess.Popen:
        """Run a Python backend (Flask/Django/FastAPI)"""
        logger.info(f"Setting up Python backend...")

        # Create virtual environment
        venv_path = project_path / 'venv'
        logger.info(f"Creating virtual environment...")
        subprocess.run(
            ['python3', '-m', 'venv', str(venv_path)],
            cwd=str(project_path),
            check=True
        )

        # Install requirements
        requirements_file = project_path / 'requirements.txt'
        if requirements_file.exists():
            logger.info(f"Installing Python dependencies...")
            pip_path = venv_path / 'bin' / 'pip'
            install_process = subprocess.run(
                [str(pip_path), 'install', '-r', 'requirements.txt'],
                cwd=str(project_path),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=120
            )

            if install_process.returncode != 0:
                error_msg = install_process.stderr.decode('utf-8')
                logger.error(f"Failed to install Python dependencies: {error_msg}")
                raise Exception(f"pip install failed: {error_msg}")

        logger.info(f"✅ Python dependencies installed")

        # Detect main file and framework
        main_files = ['main.py', 'app.py', 'server.py', 'wsgi.py']
        main_file = None
        for f in main_files:
            if (project_path / f).exists():
                main_file = f
                break

        if not main_file:
            raise Exception("No main Python file found (main.py, app.py, etc.)")

        # Check if it's FastAPI/Flask/Django
        main_content = (project_path / main_file).read_text()
        python_path = venv_path / 'bin' / 'python3'

        env = os.environ.copy()
        env['PORT'] = str(port)
        env['HOST'] = '0.0.0.0'

        if 'FastAPI' in main_content or 'fastapi' in main_content:
            # FastAPI with uvicorn
            logger.info(f"Starting FastAPI backend on port {port}...")
            uvicorn_path = venv_path / 'bin' / 'uvicorn'
            module_name = main_file.replace('.py', '')
            process = subprocess.Popen(
                [str(uvicorn_path), f'{module_name}:app', '--host', '0.0.0.0', '--port', str(port)],
                cwd=str(project_path),
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=os.setsid
            )
        elif 'Flask' in main_content or 'flask' in main_content:
            # Flask
            logger.info(f"Starting Flask backend on port {port}...")
            env['FLASK_APP'] = main_file
            env['FLASK_ENV'] = 'development'
            process = subprocess.Popen(
                [str(python_path), '-m', 'flask', 'run', '--host=0.0.0.0', f'--port={port}'],
                cwd=str(project_path),
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=os.setsid
            )
        else:
            # Generic Python app
            logger.info(f"Starting Python backend on port {port}...")
            process = subprocess.Popen(
                [str(python_path), main_file],
                cwd=str(project_path),
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=os.setsid
            )

        await asyncio.sleep(5)
        logger.info(f"✅ Python backend running on port {port}")
        return process

    async def _run_node_project(self, project_path: Path, port: int, project_type: str) -> subprocess.Popen:
        """Run a Node.js based project"""
        # Install dependencies first
        logger.info(f"Installing dependencies for {project_type} project...")
        install_process = subprocess.run(
            ['npm', 'install', '--legacy-peer-deps'],
            cwd=str(project_path),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=120
        )

        if install_process.returncode != 0:
            error_msg = install_process.stderr.decode('utf-8')
            logger.error(f"Failed to install dependencies: {error_msg}")
            raise Exception(f"npm install failed: {error_msg}")

        logger.info(f"✅ Dependencies installed successfully")

        # Determine the start command
        package_json_path = project_path / 'package.json'
        if package_json_path.exists():
            package_json = json.loads(package_json_path.read_text())
            scripts = package_json.get('scripts', {})

            # Find the dev command
            start_cmd = None
            if 'dev' in scripts:
                start_cmd = ['npm', 'run', 'dev']
            elif 'start' in scripts:
                start_cmd = ['npm', 'start']
            else:
                raise Exception("No dev or start script found in package.json")

            # Set the port environment variable
            env = os.environ.copy()
            env['PORT'] = str(port)

            # For Vite projects, add port flag
            if 'vite' in scripts.get('dev', '').lower():
                start_cmd.extend(['--', '--port', str(port), '--host', '0.0.0.0'])

            # Start the dev server
            logger.info(f"Starting {project_type} server with command: {' '.join(start_cmd)}")
            process = subprocess.Popen(
                start_cmd,
                cwd=str(project_path),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=env,
                preexec_fn=os.setsid
            )

            # Wait for server to start
            await asyncio.sleep(10)

            logger.info(f"✅ {project_type} server running on port {port}")
            return process

        raise Exception("package.json not found")

    async def _run_fullstack_project(self, project_path: Path, project_type: str) -> Tuple[subprocess.Popen, subprocess.Popen, int, int]:
        """Run a full-stack project with separate backend and frontend"""
        backend_type, frontend_type = project_type.replace('fullstack-', '').split('-')

        # Get two ports - one for backend, one for frontend
        backend_port = self._get_available_port()
        self.used_ports.add(backend_port)
        frontend_port = self._get_available_port()
        self.used_ports.add(frontend_port)

        logger.info(f"🔧 Setting up full-stack project:")
        logger.info(f"   Backend ({backend_type}): port {backend_port}")
        logger.info(f"   Frontend ({frontend_type}): port {frontend_port}")

        # Start backend first
        backend_path = project_path / 'backend'
        if backend_type == 'python':
            backend_process = await self._run_python_backend(backend_path, backend_port)
        elif backend_type == 'nodejs':
            backend_process = await self._run_node_project(backend_path, backend_port, 'nodejs')
        else:
            raise Exception(f"Unsupported backend type: {backend_type}")

        # Create .env file for frontend with backend URL
        frontend_path = project_path / 'frontend'
        frontend_env = frontend_path / '.env'
        frontend_env.write_text(f"""# Auto-generated
VITE_API_URL=http://localhost:{backend_port}
REACT_APP_API_URL=http://localhost:{backend_port}
VUE_APP_API_URL=http://localhost:{backend_port}
NEXT_PUBLIC_API_URL=http://localhost:{backend_port}
""")

        # Start frontend
        logger.info(f"🎨 Starting frontend...")
        frontend_process = await self._run_node_project(frontend_path, frontend_port, frontend_type)

        logger.info(f"✅ Full-stack project running:")
        logger.info(f"   Backend: http://localhost:{backend_port}")
        logger.info(f"   Frontend: http://localhost:{frontend_port}")

        return backend_process, frontend_process, backend_port, frontend_port

    async def deploy_project(self, project_id: str, files: Dict[str, str], project_name: str = "project") -> Dict:
        """Deploy a project and return its URL"""
        try:
            # Stop existing project if any
            await self.stop_project(project_id)

            # Detect project type
            project_type = self._detect_project_type(files)
            logger.info(f"Detected project type: {project_type}")

            # Write files to disk
            project_path = self._write_files_to_disk(project_id, files)

            # Create .env file if needed
            self._create_env_file(project_path, project_type)

            # Get available port
            port = self._get_available_port()
            self.used_ports.add(port)

            # Start the project based on type
            if project_type.startswith('fullstack-'):
                # Full-stack project with backend and frontend
                backend_process, frontend_process, backend_port, frontend_port = await self._run_fullstack_project(project_path, project_type)

                # Store both processes
                self.running_projects[project_id] = {
                    'processes': [backend_process, frontend_process],
                    'ports': [backend_port, frontend_port],
                    'type': project_type,
                    'path': str(project_path),
                    'name': project_name,
                    'backend_port': backend_port,
                    'frontend_port': frontend_port
                }

                # Return frontend URL (main entry point)
                url = f"http://localhost:{frontend_port}"

                logger.info(f"✅ Full-stack project {project_id} deployed successfully")
                logger.info(f"   Frontend: {url}")
                logger.info(f"   Backend: http://localhost:{backend_port}")

                return {
                    'success': True,
                    'url': url,
                    'port': frontend_port,
                    'backend_port': backend_port,
                    'type': project_type,
                    'project_id': project_id
                }

            elif project_type == 'static':
                process = await self._run_static_server(project_path, port)
            elif project_type == 'python':
                process = await self._run_python_backend(project_path, port)
            elif project_type in ['react', 'vue', 'angular', 'nextjs', 'nodejs']:
                process = await self._run_node_project(project_path, port, project_type)
            else:
                raise Exception(f"Unsupported project type: {project_type}")

            # Store project info (single process projects)
            self.running_projects[project_id] = {
                'process': process,
                'port': port,
                'type': project_type,
                'path': str(project_path),
                'name': project_name
            }

            # Generate URL
            url = f"http://localhost:{port}"

            logger.info(f"✅ Project {project_id} deployed successfully at {url}")

            return {
                'success': True,
                'url': url,
                'port': port,
                'type': project_type,
                'project_id': project_id
            }

        except Exception as e:
            logger.error(f"Failed to deploy project {project_id}: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }

    async def stop_project(self, project_id: str):
        """Stop a running project"""
        if project_id in self.running_projects:
            project_info = self.running_projects[project_id]

            # Check if it's a full-stack project with multiple processes
            if 'processes' in project_info:
                # Full-stack project - stop both backend and frontend
                processes = project_info['processes']
                ports = project_info['ports']

                for process in processes:
                    try:
                        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                        process.wait(timeout=5)
                    except Exception as e:
                        logger.warning(f"Error stopping process: {e}")
                        try:
                            os.killpg(os.getpgid(process.pid), signal.SIGKILL)
                        except:
                            pass

                # Clean up all ports
                for port in ports:
                    self.used_ports.discard(port)

            else:
                # Single process project
                process = project_info['process']
                port = project_info['port']

                try:
                    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                    process.wait(timeout=5)
                except Exception as e:
                    logger.warning(f"Error stopping project {project_id}: {e}")
                    try:
                        os.killpg(os.getpgid(process.pid), signal.SIGKILL)
                    except:
                        pass

                # Clean up
                self.used_ports.discard(port)

            del self.running_projects[project_id]
            logger.info(f"✅ Stopped project {project_id}")

    async def stop_all_projects(self):
        """Stop all running projects"""
        project_ids = list(self.running_projects.keys())
        for project_id in project_ids:
            await self.stop_project(project_id)
        logger.info("✅ All projects stopped")

    def get_running_projects(self) -> Dict:
        """Get info about all running projects"""
        result = {}
        for project_id, info in self.running_projects.items():
            if 'processes' in info:
                # Full-stack project
                result[project_id] = {
                    'type': info['type'],
                    'name': info['name'],
                    'frontend_url': f"http://localhost:{info['frontend_port']}",
                    'backend_url': f"http://localhost:{info['backend_port']}",
                    'frontend_port': info['frontend_port'],
                    'backend_port': info['backend_port']
                }
            else:
                # Single process project
                result[project_id] = {
                    'port': info['port'],
                    'type': info['type'],
                    'name': info['name'],
                    'url': f"http://localhost:{info['port']}"
                }
        return result

# Global instance
project_runner = ProjectRunner()
