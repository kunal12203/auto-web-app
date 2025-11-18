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
            if project_type == 'static':
                process = await self._run_static_server(project_path, port)
            elif project_type in ['react', 'vue', 'angular', 'nextjs', 'nodejs']:
                process = await self._run_node_project(project_path, port, project_type)
            else:
                raise Exception(f"Unsupported project type: {project_type}")

            # Store project info
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
            process = project_info['process']
            port = project_info['port']

            try:
                # Kill the process group
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
        return {
            project_id: {
                'port': info['port'],
                'type': info['type'],
                'name': info['name'],
                'url': f"http://localhost:{info['port']}"
            }
            for project_id, info in self.running_projects.items()
        }

# Global instance
project_runner = ProjectRunner()
