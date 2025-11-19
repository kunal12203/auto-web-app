"""
AI Response Parser - Structured JSON extraction from AI responses
Handles the new prompt system's JSON-based outputs
"""

import json
import re
import logging
from typing import Dict, List, Any, Optional, Tuple

logger = logging.getLogger(__name__)


class AIResponseParser:
    """Parse and validate AI responses in structured JSON format"""

    @staticmethod
    def extract_json(response_text: str) -> Optional[Dict]:
        """
        Extract JSON from AI response, handling markdown code blocks and malformed JSON

        Args:
            response_text: Raw text response from AI

        Returns:
            Parsed JSON dict or None if extraction fails
        """
        try:
            # Try direct JSON parse first
            return json.loads(response_text.strip())
        except json.JSONDecodeError:
            pass

        # Try extracting from markdown code block
        json_match = re.search(r'```json\s*\n(.*?)\n```', response_text, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(1))
            except json.JSONDecodeError:
                pass

        # Try extracting any JSON object (find outermost {})
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(0))
            except json.JSONDecodeError:
                pass

        logger.error("Failed to extract valid JSON from response")
        logger.debug(f"Response text: {response_text[:500]}...")
        return None

    @staticmethod
    def parse_project_structure(response_text: str) -> Optional[Dict]:
        """
        Parse the master project generation response

        Expected format:
        {
          "projectType": "react|fullstack|simple",
          "websiteType": "saas|ecommerce|...",
          "fileStructure": {...},
          "placeholders": {...},
          "customComponents": [...]
        }

        Returns:
            Parsed project structure or None
        """
        data = AIResponseParser.extract_json(response_text)

        if not data:
            return None

        # Validate required fields
        required_fields = ["projectType", "websiteType", "fileStructure"]
        if not all(field in data for field in required_fields):
            logger.error(f"Missing required fields in project structure: {required_fields}")
            return None

        # Validate project type
        valid_project_types = ["react", "fullstack", "simple"]
        if data["projectType"] not in valid_project_types:
            logger.warning(f"Invalid project type: {data['projectType']}, defaulting to 'react'")
            data["projectType"] = "react"

        # Ensure placeholders exist
        if "placeholders" not in data:
            data["placeholders"] = {}

        # Ensure customComponents exists
        if "customComponents" not in data:
            data["customComponents"] = []

        logger.info(f"✅ Parsed project structure: {data['projectType']} {data['websiteType']}")
        logger.info(f"   Files: {sum(len(files) for files in data['fileStructure'].values())} across {len(data['fileStructure'])} categories")
        logger.info(f"   Custom components: {len(data['customComponents'])}")

        return data

    @staticmethod
    def parse_update_structure(response_text: str) -> Optional[Dict]:
        """
        Parse multi-turn update response

        Expected format:
        {
          "modificationType": "update|add|delete|refactor",
          "filesToModify": [...],
          "filesToAdd": [...],
          "filesToDelete": [...],
          "dependencies": {...}
        }

        Returns:
            Parsed update structure or None
        """
        data = AIResponseParser.extract_json(response_text)

        if not data:
            return None

        # Provide defaults for optional fields
        defaults = {
            "modificationType": "update",
            "filesToModify": [],
            "filesToAdd": [],
            "filesToDelete": [],
            "dependencies": {"add": [], "remove": []}
        }

        # Merge defaults with parsed data
        for key, default_value in defaults.items():
            if key not in data:
                data[key] = default_value

        logger.info(f"✅ Parsed update structure: {data['modificationType']}")
        logger.info(f"   Modify: {len(data['filesToModify'])}, Add: {len(data['filesToAdd'])}, Delete: {len(data['filesToDelete'])}")

        return data

    @staticmethod
    def parse_file_structure_tree(response_text: str) -> Dict[str, str]:
        """
        Parse file structure tree from text format into dict

        Example input:
        📁 project-root/
        ├── 📁 src/
        │   ├── App.jsx (Main app)
        │   └── index.js

        Returns:
            Dict mapping file paths to descriptions
        """
        files = {}
        current_path = []

        lines = response_text.strip().split('\n')

        for line in lines:
            # Remove tree characters and emoji
            clean_line = re.sub(r'[📁├│└─\s]+', '', line)

            if not clean_line:
                continue

            # Extract file/folder name and description
            match = re.match(r'([^(]+)(?:\(([^)]+)\))?', clean_line)
            if match:
                name = match.group(1).strip()
                description = match.group(2).strip() if match.group(2) else ""

                # Determine if it's a file or folder
                is_folder = '📁' in line or name.endswith('/')

                if not is_folder and name:
                    # Calculate full path based on indentation
                    full_path = name
                    files[full_path] = description

        logger.info(f"✅ Parsed file tree: {len(files)} files identified")
        return files

    @staticmethod
    def parse_template_selection(response_text: str) -> Optional[str]:
        """
        Parse backend template selection response

        Expected: "category/TemplateName"

        Returns:
            Template path or None
        """
        # Clean response
        template_path = response_text.strip()

        # Remove markdown code blocks
        template_path = re.sub(r'```\w*\n?', '', template_path).strip()

        # Remove quotes if present
        template_path = template_path.strip('"\'')

        # Validate format: category/TemplateName
        if '/' in template_path and len(template_path.split('/')) == 2:
            logger.info(f"✅ Parsed template selection: {template_path}")
            return template_path

        logger.warning(f"Invalid template path format: {template_path}")
        return None

    @staticmethod
    def parse_placeholder_values(response_text: str) -> Dict[str, str]:
        """
        Parse placeholder customization values

        Expected JSON:
        {
          "LOGO_TEXT": "value",
          "PRIMARY_COLOR": "#3B82F6",
          ...
        }

        Returns:
            Dict of placeholder values
        """
        data = AIResponseParser.extract_json(response_text)

        if not data or not isinstance(data, dict):
            logger.warning("Failed to parse placeholder values, using defaults")
            return {}

        logger.info(f"✅ Parsed {len(data)} placeholder values")
        return data

    @staticmethod
    def extract_file_content(response_text: str, expected_extension: str = None) -> str:
        """
        Extract clean file content from AI response
        Handles markdown code blocks and formatting

        Args:
            response_text: Raw AI response
            expected_extension: Expected file extension (.jsx, .js, .css, etc.)

        Returns:
            Clean file content
        """
        content = response_text.strip()

        # Remove markdown code blocks
        patterns = [
            r'```jsx\n(.*?)\n```',
            r'```javascript\n(.*?)\n```',
            r'```js\n(.*?)\n```',
            r'```css\n(.*?)\n```',
            r'```html\n(.*?)\n```',
            r'```sql\n(.*?)\n```',
            r'```json\n(.*?)\n```',
            r'```\n(.*?)\n```',
        ]

        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL)
            if match:
                content = match.group(1)
                break
        else:
            # Try removing any remaining backticks
            if content.startswith('```'):
                lines = content.split('\n')
                content = '\n'.join(lines[1:])
            if content.endswith('```'):
                content = content.rsplit('```', 1)[0]

        return content.strip()

    @staticmethod
    def validate_component_completeness(content: str, component_name: str) -> Tuple[bool, str]:
        """
        Validate that a React component is complete

        Returns:
            (is_complete, error_message)
        """
        issues = []

        # Check for balanced braces
        if content.count('{') != content.count('}'):
            issues.append(f"Unbalanced braces: {content.count('{')} open, {content.count('}')} close")

        # Check for balanced brackets
        if content.count('[') != content.count(']'):
            issues.append(f"Unbalanced brackets: {content.count('[')} open, {content.count(']')} close")

        # Check for balanced parentheses
        if content.count('(') != content.count(')'):
            issues.append(f"Unbalanced parentheses: {content.count('(')} open, {content.count(')')} close")

        # Check for export
        if 'export default' not in content and f'export const {component_name}' not in content:
            issues.append("Missing export statement")

        # Check for component definition
        if f'function {component_name}' not in content and f'const {component_name}' not in content:
            issues.append(f"Missing component definition for {component_name}")

        # Check minimum length (very short files are likely truncated)
        if len(content) < 100:
            issues.append(f"File too short ({len(content)} chars) - likely truncated")

        # Check for common truncation indicators
        truncation_indicators = [
            '...',
            '// ... rest of',
            '/* ... */',
            '// TODO',
            '// Add more',
        ]

        for indicator in truncation_indicators:
            if indicator in content:
                issues.append(f"Possible truncation detected: '{indicator}'")

        if issues:
            return False, "; ".join(issues)

        return True, ""

    @staticmethod
    def extract_imports(content: str) -> List[str]:
        """Extract all import statements from code"""
        imports = []

        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('import '):
                imports.append(line)

        return imports

    @staticmethod
    def extract_dependencies_from_imports(imports: List[str]) -> List[str]:
        """Extract npm package names from import statements"""
        dependencies = set()

        for imp in imports:
            # Match: import X from 'package-name'
            match = re.search(r"from ['\"]([^'\"./][^'\"]*)['\"]", imp)
            if match:
                pkg = match.group(1)
                # Handle scoped packages like @org/package
                if '/' in pkg and not pkg.startswith('@'):
                    pkg = pkg.split('/')[0]
                dependencies.add(pkg)

        return list(dependencies)


# Convenience functions for common parsing tasks

def parse_project_from_ai(response: str) -> Optional[Dict]:
    """Quick helper to parse project structure"""
    return AIResponseParser.parse_project_structure(response)


def parse_update_from_ai(response: str) -> Optional[Dict]:
    """Quick helper to parse update structure"""
    return AIResponseParser.parse_update_structure(response)


def extract_code_from_ai(response: str, extension: str = None) -> str:
    """Quick helper to extract code"""
    return AIResponseParser.extract_file_content(response, extension)


def validate_react_component(code: str, name: str) -> Tuple[bool, str]:
    """Quick helper to validate React component"""
    return AIResponseParser.validate_component_completeness(code, name)
