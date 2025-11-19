"""
HIGH-QUALITY HYBRID GENERATION SYSTEM
Templates for speed + LLM for quality = Best of both worlds

Strategy:
1. Templates provide STRUCTURE (fast scaffolding)
2. LLM provides QUALITY (customization, correctness, polish)
3. LLM enhances template output to match user's exact requirements
4. Never compromise quality for token savings
"""

from typing import Dict, List, Optional, Tuple
import logging
from anthropic import Anthropic
import os
import json

logger = logging.getLogger(__name__)

# Initialize Claude client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def generate_high_quality_react_project(files: Dict[str, str], prompt: str) -> Dict[str, str]:
    """
    Generate HIGH-QUALITY React project
    Uses hybrid approach: templates for structure, LLM for quality

    Philosophy: QUALITY FIRST, tokens second
    """

    logger.info("🎨 HIGH-QUALITY GENERATION MODE")
    logger.info("   Strategy: Templates + LLM Enhancement")
    logger.info("=" * 80)

    # STEP 1: Analyze requirements with LLM
    logger.info("📋 Step 1: Analyzing requirements with LLM...")
    requirements = analyze_requirements_with_llm(prompt)

    logger.info(f"   Website Type: {requirements['website_type']}")
    logger.info(f"   Components: {', '.join(requirements['components'])}")
    logger.info(f"   Features: {', '.join(requirements['features'])}")

    # STEP 2: Generate components with LLM (high quality)
    logger.info("\n🤖 Step 2: Generating high-quality components with LLM...")

    components = {}
    for component_name in requirements['components']:
        logger.info(f"   Generating {component_name}...")

        component_code = generate_component_with_llm(
            component_name=component_name,
            prompt=prompt,
            requirements=requirements
        )

        if component_code:
            components[component_name] = component_code
            files[f"src/components/{component_name}.jsx"] = component_code
            logger.info(f"   ✅ {component_name} generated ({len(component_code)} chars)")
        else:
            logger.warning(f"   ⚠️  {component_name} generation failed, skipping")

    # STEP 3: Generate App.jsx
    logger.info("\n⚙️  Step 3: Generating App.jsx...")
    app_jsx = generate_app_jsx(components, prompt, requirements)
    files["src/App.jsx"] = app_jsx
    logger.info(f"   ✅ App.jsx generated ({len(app_jsx)} chars)")

    # STEP 4: Generate high-quality CSS
    logger.info("\n🎨 Step 4: Generating professional CSS...")
    app_css = generate_css_with_llm(prompt, requirements, list(components.keys()))
    files["src/App.css"] = app_css
    logger.info(f"   ✅ CSS generated ({len(app_css)} chars)")

    logger.info("\n✅ HIGH-QUALITY PROJECT COMPLETE!")
    logger.info(f"   Total components: {len(components)}")
    logger.info("=" * 80)

    return files


def analyze_requirements_with_llm(prompt: str) -> Dict:
    """Use LLM to deeply analyze what the user wants"""

    analysis_prompt = f"""Analyze this website request and extract detailed requirements.

User Request: "{prompt}"

Return ONLY valid JSON with this structure:
{{
  "website_type": "ecommerce|portfolio|saas|restaurant|fitness|business|general",
  "components": ["ComponentName1", "ComponentName2", ...],
  "features": ["feature1", "feature2", ...],
  "style": "modern|minimal|bold|elegant|playful",
  "color_scheme": "primary color suggestion",
  "key_sections": ["section1", "section2", ...]
}}

Components should be React component names (PascalCase):
- Hero, Header, Footer, Features, Pricing, Testimonials, Gallery,
- ProductCard, ContactForm, AboutSection, Newsletter, etc.

Be specific and comprehensive. Include all components needed for a complete, professional website."""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1500,
            messages=[{"role": "user", "content": analysis_prompt}]
        )

        result = response.content[0].text.strip()

        # Clean JSON
        if result.startswith("```json"):
            result = result[7:]
        elif result.startswith("```"):
            result = result[3:]
        if result.endswith("```"):
            result = result[:-3]

        requirements = json.loads(result.strip())

        # Ensure we have essential components
        if 'components' not in requirements or len(requirements['components']) == 0:
            requirements['components'] = ['Header', 'Hero', 'Features', 'Footer']

        return requirements

    except Exception as e:
        logger.error(f"Requirements analysis failed: {e}")
        # Fallback
        return {
            "website_type": "general",
            "components": ["Header", "Hero", "Features", "Footer"],
            "features": [],
            "style": "modern",
            "color_scheme": "#667eea",
            "key_sections": []
        }


def generate_component_with_llm(
    component_name: str,
    prompt: str,
    requirements: Dict
) -> Optional[str]:
    """
    Generate a single high-quality React component with LLM

    Uses larger token budget for quality
    Includes proper error handling, responsiveness, accessibility
    """

    component_prompt = f"""Generate a PROFESSIONAL, COMPLETE React component for: {component_name}

Context:
- User wants: {prompt}
- Website type: {requirements.get('website_type', 'general')}
- Style: {requirements.get('style', 'modern')}
- Color scheme: {requirements.get('color_scheme', '#667eea')}

Requirements for {component_name}:
✅ MUST be a complete, production-ready React functional component
✅ MUST use modern React hooks (useState, useEffect if needed)
✅ MUST be fully responsive (mobile-first design)
✅ MUST have professional styling with Tailwind-style classes
✅ MUST include proper accessibility (ARIA labels, semantic HTML)
✅ MUST have smooth animations and transitions
✅ MUST be pixel-perfect and polished
✅ MUST match the user's requirements exactly

Code quality:
- Clean, readable code with comments
- Proper JSX formatting
- No placeholder content - use realistic, professional copy
- Export the component properly

Return ONLY the complete .jsx file content, no markdown, no explanations."""

    max_retries = 2
    for attempt in range(max_retries):
        try:
            # Use larger token budget for quality
            tokens = 5000 if attempt == 0 else 6000

            response = client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=tokens,
                messages=[{"role": "user", "content": component_prompt}]
            )

            component_code = response.content[0].text.strip()

            # Clean markdown
            if component_code.startswith("```jsx") or component_code.startswith("```javascript"):
                component_code = component_code.split("\n", 1)[1]
            if component_code.startswith("```"):
                component_code = component_code.split("\n", 1)[1]
            if component_code.endswith("```"):
                component_code = component_code.rsplit("```", 1)[0]

            component_code = component_code.strip()

            # Basic validation
            if len(component_code) > 100 and 'export' in component_code:
                return component_code
            else:
                if attempt < max_retries - 1:
                    logger.warning(f"   Component incomplete, retrying...")
                    continue

        except Exception as e:
            logger.error(f"   Error generating {component_name}: {e}")
            if attempt >= max_retries - 1:
                return None

    return None


def generate_app_jsx(
    components: Dict[str, str],
    prompt: str,
    requirements: Dict
) -> str:
    """Generate App.jsx that intelligently uses all components"""

    component_names = list(components.keys())

    app_prompt = f"""Generate a COMPLETE React App.jsx file.

User wants: {prompt}

Available components: {', '.join(component_names)}

Requirements:
✅ Import and use ALL components in a logical order
✅ Add smooth scroll behavior
✅ Include React Router if needed for multi-page
✅ Add state management if components need to share data
✅ Professional, clean code structure
✅ Proper error boundaries
✅ COMPLETE code - no truncation

Return ONLY the complete App.jsx content, no markdown."""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=4000,
            messages=[{"role": "user", "content": app_prompt}]
        )

        app_code = response.content[0].text.strip()

        # Clean markdown
        if app_code.startswith("```"):
            app_code = app_code.split("\n", 1)[1]
        if app_code.endswith("```"):
            app_code = app_code.rsplit("```", 1)[0]

        return app_code.strip()

    except Exception as e:
        logger.error(f"App.jsx generation failed: {e}")

        # Fallback: simple App.jsx
        imports = "\n".join([f"import {name} from './components/{name}'" for name in component_names])
        components_jsx = "\n      ".join([f"<{name} />" for name in component_names])

        return f"""import {{ useState }} from 'react'
import './App.css'
{imports}

function App() {{
  return (
    <div className="App">
      {components_jsx}
    </div>
  )
}}

export default App
"""


def generate_css_with_llm(
    prompt: str,
    requirements: Dict,
    component_names: List[str]
) -> str:
    """Generate professional, comprehensive CSS"""

    css_prompt = f"""Generate COMPLETE, PROFESSIONAL CSS for this React app.

User wants: {prompt}
Components: {', '.join(component_names)}
Style: {requirements.get('style', 'modern')}
Color scheme: {requirements.get('color_scheme', '#667eea')}

Requirements:
✅ Modern, responsive design (mobile-first)
✅ Professional color palette and typography
✅ Smooth animations and transitions
✅ Proper spacing and layout
✅ Hover states and interactions
✅ CSS Grid and Flexbox for layout
✅ Media queries for all screen sizes
✅ COMPLETE styles for ALL components
✅ No Tailwind - pure CSS

Return ONLY the complete CSS, no markdown, no explanations."""

    max_retries = 2
    for attempt in range(max_retries):
        try:
            tokens = 6000 if attempt == 0 else 8000

            response = client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=tokens,
                messages=[{"role": "user", "content": css_prompt}]
            )

            css_code = response.content[0].text.strip()

            # Clean markdown
            if css_code.startswith("```css"):
                css_code = css_code[6:]
            elif css_code.startswith("```"):
                css_code = css_code[3:]
            if css_code.endswith("```"):
                css_code = css_code[:-3]

            css_code = css_code.strip()

            if len(css_code) > 500:
                return css_code
            else:
                if attempt < max_retries - 1:
                    logger.warning("   CSS too short, retrying...")
                    continue

        except Exception as e:
            logger.error(f"CSS generation failed: {e}")

    # Fallback CSS
    return """* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  line-height: 1.6;
  color: #333;
}

.App {
  min-height: 100vh;
}

/* Add your custom styles here */
"""
