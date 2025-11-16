"""
Project Memory Management - Token-Optimized Context Storage
Prevents AI hallucination during updates by maintaining compressed project state
"""

import json
from typing import Dict, List, Optional
from datetime import datetime
import hashlib
import logging

# Configure logging
logger = logging.getLogger(__name__)


class ProjectMemory:
    """
    Stores compressed project metadata to provide context for updates
    Token usage: ~100-200 tokens (vs sending entire project ~5,000+ tokens)
    """

    def __init__(self):
        self.sessions: Dict[str, dict] = {}

    def create_project_fingerprint(
        self,
        project_name: str,
        project_type: str,
        files: Dict[str, str],
        payment_gateway: Optional[str] = None,
        original_prompt: str = ""
    ) -> dict:
        """
        Create ultra-compressed project metadata

        Token cost: ~150 tokens when sent to Claude (vs ~5,000 for full project)

        Returns:
            Compressed fingerprint with essential context
        """
        logger.info("🧠 Creating project memory fingerprint...")
        logger.debug(f"   Project: {project_name}")
        logger.debug(f"   Type: {project_type}")
        logger.debug(f"   Files: {len(files)}")

        # Extract tech stack from files
        tech_stack = self._detect_tech_stack(files)
        logger.debug(f"   Detected tech stack: {tech_stack}")

        # Create compressed file structure (just paths, no content)
        file_structure = list(files.keys())

        # Detect key dependencies
        dependencies = self._extract_dependencies(files)
        logger.debug(f"   Dependencies: {len(dependencies)} found")

        # Create fingerprint
        fingerprint = {
            "project_name": project_name,
            "project_type": project_type,  # simple/react/fullstack
            "tech_stack": tech_stack,  # ["react", "vite", "fastapi", "tailwind"]
            "file_structure": file_structure,  # ["src/App.jsx", "src/index.css", ...]
            "dependencies": dependencies,  # {"react": "^18.2.0", ...}
            "payment_gateway": payment_gateway,  # stripe/paypal/razorpay/none
            "original_prompt": original_prompt[:500],  # Truncate to save tokens
            "created_at": datetime.now().isoformat(),
            "file_count": len(files),
            "total_lines": sum(content.count('\n') for content in files.values())
        }

        # Generate session ID
        session_id = self._generate_session_id(project_name)
        self.sessions[session_id] = fingerprint
        logger.info(f"✅ Memory fingerprint created: {session_id}")
        logger.info(f"   Active sessions: {len(self.sessions)}")

        return {
            "session_id": session_id,
            "fingerprint": fingerprint
        }

    def get_update_context(
        self,
        session_id: str,
        file_to_update: str,
        current_file_content: str
    ) -> str:
        """
        Generate compressed context for file updates

        Token cost: ~200-300 tokens (vs ~2,000+ without memory)

        Returns:
            Compressed context string for Claude
        """
        logger.info(f"📝 Generating update context for: {file_to_update}")
        logger.debug(f"   Session ID: {session_id}")

        if session_id not in self.sessions:
            logger.warning(f"⚠️  Session {session_id} not found! Using fallback context.")
            return self._fallback_context(file_to_update, current_file_content)

        fingerprint = self.sessions[session_id]
        logger.debug(f"   Found session: {fingerprint['project_name']} ({fingerprint['project_type']})")

        # ULTRA COMPRESSED CONTEXT (bullet points, abbreviations)
        context = f"""PROJECT CONTEXT (don't recreate, UPDATE only):
Type: {fingerprint['project_type']}
Stack: {', '.join(fingerprint['tech_stack'])}
Payment: {fingerprint['payment_gateway'] or 'none'}
Files: {fingerprint['file_count']} files
Structure: {', '.join(fingerprint['file_structure'][:10])}{'...' if len(fingerprint['file_structure']) > 10 else ''}

UPDATING: {file_to_update}

CURRENT CODE:
{current_file_content[:1500]}
{'...[truncated]' if len(current_file_content) > 1500 else ''}

RULES:
- Keep existing imports/structure
- Don't hallucinate new files
- Match current coding style
- Preserve dependencies"""

        logger.info(f"✅ Generated update context ({len(context)} chars, ~{len(context)//4} tokens)")
        return context

    def get_error_fix_context(
        self,
        session_id: str,
        error_info: dict,
        relevant_file: str,
        file_content: str
    ) -> str:
        """
        Generate compressed context for error fixing

        Token cost: ~250-350 tokens (vs ~2,000+ without memory)
        """
        logger.info(f"🔧 Generating error fix context for: {relevant_file}")
        logger.debug(f"   Session ID: {session_id}")
        logger.debug(f"   Error: {error_info.get('message', 'Unknown')}")

        if session_id not in self.sessions:
            logger.warning(f"⚠️  Session {session_id} not found! Using fallback context.")
            return self._fallback_error_context(error_info, relevant_file, file_content)

        fingerprint = self.sessions[session_id]
        logger.debug(f"   Found session: {fingerprint['project_name']} ({fingerprint['project_type']})")

        # COMPRESSED ERROR CONTEXT
        context = f"""FIX ERROR (don't regenerate):
Type: {fingerprint['project_type']}
Stack: {', '.join(fingerprint['tech_stack'])}

ERROR:
{error_info.get('message', 'Unknown error')}
File: {error_info.get('filename', relevant_file)}
Line: {error_info.get('lineno', 'unknown')}

CURRENT CODE ({relevant_file}):
{file_content[:1000]}
{'...[truncated]' if len(file_content) > 1000 else ''}

FIX:
- Minimal change only
- Keep existing structure
- Match style"""

        logger.info(f"✅ Generated error fix context ({len(context)} chars, ~{len(context)//4} tokens)")
        return context

    def _detect_tech_stack(self, files: Dict[str, str]) -> List[str]:
        """Detect technologies used in project"""
        stack = set()

        # Check file extensions
        for path in files.keys():
            if path.endswith('.jsx') or path.endswith('.tsx'):
                stack.add('react')
            if 'vite.config' in path:
                stack.add('vite')
            if path.endswith('.py'):
                stack.add('python')
            if 'fastapi' in files.get(path, '').lower():
                stack.add('fastapi')

        # Check content for frameworks
        all_content = ' '.join(files.values()).lower()
        if 'tailwind' in all_content or '@tailwind' in all_content:
            stack.add('tailwind')
        if 'stripe' in all_content:
            stack.add('stripe')
        if 'paypal' in all_content:
            stack.add('paypal')
        if 'razorpay' in all_content:
            stack.add('razorpay')
        if 'docker' in all_content or any('Dockerfile' in p for p in files.keys()):
            stack.add('docker')

        return sorted(list(stack))

    def _extract_dependencies(self, files: Dict[str, str]) -> Dict[str, str]:
        """Extract key dependencies from package.json or requirements.txt"""
        deps = {}

        # Check package.json
        if 'package.json' in files:
            try:
                pkg = json.loads(files['package.json'])
                deps.update(pkg.get('dependencies', {}))
            except:
                pass

        # Check requirements.txt
        if 'requirements.txt' in files:
            for line in files['requirements.txt'].split('\n'):
                line = line.strip()
                if line and not line.startswith('#'):
                    if '==' in line:
                        name, version = line.split('==', 1)
                        deps[name] = version

        return deps

    def _generate_session_id(self, project_name: str) -> str:
        """Generate unique session ID"""
        timestamp = datetime.now().isoformat()
        hash_input = f"{project_name}-{timestamp}"
        return hashlib.md5(hash_input.encode()).hexdigest()[:16]

    def _fallback_context(self, file_to_update: str, current_content: str) -> str:
        """Fallback context when no session found"""
        return f"""UPDATING: {file_to_update}

CURRENT CODE:
{current_content[:1500]}
{'...[truncated]' if len(current_content) > 1500 else ''}

RULES:
- Minimal changes only
- Keep existing structure"""

    def _fallback_error_context(self, error_info: dict, file: str, content: str) -> str:
        """Fallback error context"""
        return f"""FIX ERROR:
{error_info.get('message', 'Unknown')}

CODE ({file}):
{content[:1000]}

FIX: Minimal change only"""


# Global instance
project_memory = ProjectMemory()


def create_compressed_generation_context(
    project_type: str,
    original_prompt: str,
    existing_files: Optional[Dict[str, str]] = None
) -> str:
    """
    Create compressed context for generation (when building from scratch)

    Token cost: ~300-500 tokens (vs ~5,000+ for verbose prompts)
    """

    # If updating existing project, add context
    if existing_files:
        file_list = ', '.join(list(existing_files.keys())[:8])
        file_context = f"\nEXISTING FILES: {file_list}\nDON'T recreate - BUILD ON existing."
    else:
        file_context = ""

    context = f"""BUILD {project_type.upper()} PROJECT:

REQUEST: {original_prompt[:800]}

GENERATE:
- Production-ready code
- Modern best practices
- Responsive design
- Clean structure{file_context}

OUTPUT: Complete files only, no explanations."""

    return context
