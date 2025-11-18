"""
Structured Project Generator - Uses JSON-based prompts for better control
Leverages 2,200+ templates with clear file structure outputs
Supports multi-turn refinement with structured updates
"""

import logging
import json
from typing import Dict, List, Optional, Any
from anthropic import Anthropic
import os

from ai_prompts import (
    format_master_prompt,
    format_update_prompt,
    format_component_prompt,
    format_file_structure_prompt,
    format_customization_prompt,
    WEBSITE_TYPES
)
from ai_response_parser import (
    AIResponseParser,
    parse_project_from_ai,
    parse_update_from_ai,
    extract_code_from_ai,
    validate_react_component
)
from intelligent_templates import (
    analyze_prompt_for_components,
    match_components_with_templates,
    load_matched_components
)

logger = logging.getLogger(__name__)

# Initialize Claude client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


class StructuredProjectGenerator:
    """
    Advanced project generator using structured JSON prompts

    This generator:
    1. Gets clear file structure from AI first
    2. Maps to 2,200+ template library
    3. Generates only what's not in templates
    4. Supports multi-turn updates with structured changes
    """

    def __init__(self):
        self.parser = AIResponseParser()

    def generate_project_structure(self, user_prompt: str) -> Optional[Dict]:
        """
        Step 1: Get structured project plan from AI

        Returns JSON with:
        - projectType
        - websiteType
        - fileStructure (with template mappings)
        - placeholders
        - customComponents
        """
        logger.info("🎯 Step 1: Getting structured project plan from AI...")

        prompt = format_master_prompt(user_prompt)

        try:
            response = client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}]
            )

            response_text = response.content[0].text

            # Parse the structured response
            project_structure = parse_project_from_ai(response_text)

            if not project_structure:
                logger.error("Failed to parse project structure from AI response")
                logger.debug(f"Raw response: {response_text[:500]}...")
                return None

            logger.info(f"✅ Project structure received:")
            logger.info(f"   Type: {project_structure['projectType']}")
            logger.info(f"   Website: {project_structure['websiteType']}")
            logger.info(f"   Files: {len(project_structure.get('fileStructure', {}))} categories")
            logger.info(f"   Custom: {len(project_structure.get('customComponents', []))} components")

            return project_structure

        except Exception as e:
            logger.error(f"Error getting project structure: {e}")
            return None

    def map_to_templates(self, file_structure: Dict) -> Dict[str, Any]:
        """
        Step 2: Map file structure to our template library

        Returns:
        - matched: Files that can use templates
        - generate: Files that need AI generation
        - templates: Template metadata for matched files
        """
        logger.info("📚 Step 2: Mapping files to template library...")

        matched_files = {}
        files_to_generate = {}
        template_metadata = {}

        # Process frontend files
        if 'frontend' in file_structure:
            frontend_files = file_structure['frontend']

            for file_path, file_info in frontend_files.items():
                template_name = file_info.get('template')

                if template_name and 'customize' in file_info:
                    # Can use template with customization
                    matched_files[file_path] = {
                        'template': template_name,
                        'customize': file_info['customize']
                    }
                    logger.info(f"   ✅ {file_path} -> template: {template_name}")
                else:
                    # Need to generate
                    files_to_generate[file_path] = file_info
                    logger.info(f"   🤖 {file_path} -> needs generation")

        # Process backend files
        if 'backend' in file_structure:
            backend_files = file_structure['backend']

            for file_path, file_info in backend_files.items():
                template_name = file_info.get('template')

                if template_name:
                    matched_files[file_path] = {
                        'template': template_name,
                        'features': file_info.get('features', [])
                    }
                    logger.info(f"   ✅ {file_path} -> template: {template_name}")
                else:
                    files_to_generate[file_path] = file_info
                    logger.info(f"   🤖 {file_path} -> needs generation")

        # Process database files
        if 'database' in file_structure:
            database_files = file_structure['database']

            for file_path, file_info in database_files.items():
                template_name = file_info.get('template')

                if template_name:
                    matched_files[file_path] = {
                        'template': template_name,
                        'tables': file_info.get('tables', [])
                    }
                    logger.info(f"   ✅ {file_path} -> template: {template_name}")
                else:
                    files_to_generate[file_path] = file_info
                    logger.info(f"   🤖 {file_path} -> needs generation")

        logger.info(f"✅ Mapping complete: {len(matched_files)} from templates, {len(files_to_generate)} to generate")

        return {
            'matched': matched_files,
            'generate': files_to_generate,
            'metadata': template_metadata
        }

    def load_template_files(
        self,
        matched_files: Dict,
        placeholders: Dict[str, str]
    ) -> Dict[str, str]:
        """
        Step 3: Load and customize templates

        Returns dict of file_path -> content
        """
        logger.info(f"📥 Step 3: Loading {len(matched_files)} files from templates...")

        loaded_files = {}

        for file_path, file_info in matched_files.items():
            template_name = file_info['template']
            customization = file_info.get('customize', {})

            try:
                # Load the template
                # This would interface with our existing template system
                # For now, we'll use the existing load_matched_components

                component_name = os.path.basename(file_path).replace('.jsx', '')

                # Merge customization with placeholders
                all_placeholders = {**placeholders, **customization}

                # Load from template library
                if 'components' in template_name.lower():
                    # Use existing component loading system
                    loaded = load_matched_components(
                        {component_name: template_name},
                        all_placeholders
                    )

                    if component_name in loaded:
                        loaded_files[file_path] = loaded[component_name]
                        logger.info(f"   ✅ {file_path} loaded from template")
                    else:
                        logger.warning(f"   ⚠️ Failed to load {file_path} from template")

            except Exception as e:
                logger.error(f"   ❌ Error loading {file_path}: {e}")

        logger.info(f"✅ Loaded {len(loaded_files)} files from templates")

        return loaded_files

    def generate_custom_files(
        self,
        files_to_generate: Dict,
        user_prompt: str,
        website_type: str,
        placeholders: Dict[str, str]
    ) -> Dict[str, str]:
        """
        Step 4: Generate custom files with AI

        Uses component-specific prompts with retry logic
        """
        logger.info(f"🤖 Step 4: Generating {len(files_to_generate)} custom files with AI...")

        generated_files = {}

        primary_color = placeholders.get('PRIMARY_COLOR', '#3B82F6')
        secondary_color = placeholders.get('SECONDARY_COLOR', '#8B5CF6')

        for file_path, file_info in files_to_generate.items():
            logger.info(f"   Generating {file_path}...")

            component_name = os.path.basename(file_path).replace('.jsx', '').replace('.js', '')
            component_purpose = file_info.get('reason', file_info.get('template', ''))

            # Generate with retry
            max_retries = 2

            for attempt in range(max_retries):
                tokens = 3000 if attempt == 0 else 4500
                retry_note = "\n\nIMPORTANT: This is a retry - previous attempt was incomplete. Generate the ENTIRE file." if attempt > 0 else ""

                prompt = format_component_prompt(
                    component_name=component_name,
                    user_prompt=user_prompt,
                    website_type=website_type,
                    component_purpose=component_purpose,
                    primary_color=primary_color,
                    secondary_color=secondary_color,
                    retry_note=retry_note
                )

                try:
                    response = client.messages.create(
                        model="claude-sonnet-4-5",
                        max_tokens=tokens,
                        messages=[{"role": "user", "content": prompt}]
                    )

                    code = extract_code_from_ai(response.content[0].text, '.jsx')

                    # Validate completeness
                    is_complete, error_msg = validate_react_component(code, component_name)

                    if is_complete:
                        generated_files[file_path] = code
                        logger.info(f"      ✅ Generated successfully ({len(code)} chars)")
                        break
                    else:
                        logger.warning(f"      ⚠️ Incomplete (attempt {attempt + 1}/{max_retries}): {error_msg}")

                        if attempt == max_retries - 1:
                            # Last attempt failed, use it anyway with warning
                            generated_files[file_path] = code
                            logger.warning(f"      ⚠️ Using potentially incomplete file")

                except Exception as e:
                    logger.error(f"      ❌ Error generating {file_path}: {e}")

                    if attempt == max_retries - 1:
                        # Create fallback placeholder
                        generated_files[file_path] = self._create_fallback_component(component_name)

        logger.info(f"✅ Generated {len(generated_files)} custom files")

        return generated_files

    def generate_complete_project(self, user_prompt: str) -> Optional[Dict[str, str]]:
        """
        Main method: Generate complete project using structured approach

        Flow:
        1. Get structured plan from AI
        2. Map to template library
        3. Load templates
        4. Generate custom files
        5. Combine and return
        """
        logger.info("🚀 Starting structured project generation...")
        logger.info(f"   Prompt: {user_prompt[:100]}...")

        # Step 1: Get project structure
        project_structure = self.generate_project_structure(user_prompt)

        if not project_structure:
            logger.error("❌ Failed to get project structure")
            return None

        project_type = project_structure['projectType']
        website_type = project_structure['websiteType']
        file_structure = project_structure['fileStructure']
        placeholders = project_structure.get('placeholders', {})

        # Step 2: Map to templates
        mapping = self.map_to_templates(file_structure)

        # Step 3: Load templates
        template_files = self.load_template_files(
            mapping['matched'],
            placeholders
        )

        # Step 4: Generate custom files
        generated_files = self.generate_custom_files(
            mapping['generate'],
            user_prompt,
            website_type,
            placeholders
        )

        # Step 5: Combine all files
        all_files = {**template_files, **generated_files}

        # Add essential config files
        all_files.update(self._create_config_files(project_type, all_files))

        logger.info(f"✅ Project generation complete:")
        logger.info(f"   Total files: {len(all_files)}")
        logger.info(f"   From templates: {len(template_files)}")
        logger.info(f"   Generated: {len(generated_files)}")

        return all_files

    def update_existing_project(
        self,
        modification_request: str,
        project_type: str,
        session_id: str,
        current_files: Dict[str, str],
        project_memory: str
    ) -> Optional[Dict]:
        """
        Handle multi-turn updates with structured changes

        Returns:
        - filesToModify: List of files with changes
        - filesToAdd: New files to create
        - filesToDelete: Files to remove
        """
        logger.info("🔄 Processing multi-turn update request...")

        prompt = format_update_prompt(
            modification_request=modification_request,
            project_type=project_type,
            session_id=session_id,
            file_count=len(current_files),
            project_memory=project_memory
        )

        try:
            response = client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=3000,
                messages=[{"role": "user", "content": prompt}]
            )

            update_structure = parse_update_from_ai(response.content[0].text)

            if not update_structure:
                logger.error("Failed to parse update structure")
                return None

            logger.info(f"✅ Update structure received:")
            logger.info(f"   Type: {update_structure['modificationType']}")
            logger.info(f"   Modify: {len(update_structure['filesToModify'])} files")
            logger.info(f"   Add: {len(update_structure['filesToAdd'])} files")
            logger.info(f"   Delete: {len(update_structure['filesToDelete'])} files")

            return update_structure

        except Exception as e:
            logger.error(f"Error processing update: {e}")
            return None

    def _create_config_files(self, project_type: str, project_files: Dict[str, str]) -> Dict[str, str]:
        """Create essential config files (package.json, vite.config, etc.)"""
        config_files = {}

        if project_type == 'react' or project_type == 'fullstack':
            # Analyze imports to determine dependencies
            all_imports = []
            for content in project_files.values():
                imports = self.parser.extract_imports(content)
                all_imports.extend(imports)

            dependencies = self.parser.extract_dependencies_from_imports(all_imports)

            # Add React essentials
            base_deps = ["react", "react-dom"]
            all_deps = list(set(base_deps + dependencies))

            config_files['package.json'] = self._generate_package_json(all_deps)
            config_files['vite.config.js'] = self._generate_vite_config()
            config_files['index.html'] = self._generate_index_html()

        return config_files

    def _generate_package_json(self, dependencies: List[str]) -> str:
        """Generate package.json with detected dependencies"""
        deps = {dep: "latest" for dep in dependencies}

        package = {
            "name": "generated-project",
            "private": True,
            "version": "0.0.0",
            "type": "module",
            "scripts": {
                "dev": "vite",
                "build": "vite build",
                "preview": "vite preview"
            },
            "dependencies": deps,
            "devDependencies": {
                "@vitejs/plugin-react": "^4.3.1",
                "vite": "^5.3.1"
            }
        }

        return json.dumps(package, indent=2)

    def _generate_vite_config(self) -> str:
        """Generate vite.config.js"""
        return """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true
  }
})
"""

    def _generate_index_html(self) -> str:
        """Generate index.html"""
        return """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Generated App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
"""

    def _create_fallback_component(self, component_name: str) -> str:
        """Create a simple fallback component if generation fails"""
        return f"""import React from 'react'

export default function {component_name}({{ children, ...props }}) {{
  return (
    <div className="{component_name.lower()}" {{...props}}>
      <h2>{component_name}</h2>
      {{children}}
    </div>
  )
}}
"""


# Singleton instance
structured_generator = StructuredProjectGenerator()


# Convenience functions
def generate_project_structured(user_prompt: str) -> Optional[Dict[str, str]]:
    """Generate project using structured approach"""
    return structured_generator.generate_complete_project(user_prompt)


def update_project_structured(
    modification_request: str,
    project_type: str,
    session_id: str,
    current_files: Dict[str, str],
    project_memory: str
) -> Optional[Dict]:
    """Update project using structured approach"""
    return structured_generator.update_existing_project(
        modification_request,
        project_type,
        session_id,
        current_files,
        project_memory
    )
