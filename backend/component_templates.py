"""
Component Library System - Mix and match reusable components
Zero tokens for structure - loads complete components from disk
Smart mapping system to select relevant components for any website type
"""

from pathlib import Path
from typing import Dict, Optional, List
import json
import re

TEMPLATES_DIR = Path(__file__).parent / "templates"
COMPONENTS_DIR = TEMPLATES_DIR / "components"
STYLES_DIR = TEMPLATES_DIR / "styles"
MAPPINGS_FILE = TEMPLATES_DIR / "mappings.json"


def load_mappings() -> Dict:
    """Load component mappings configuration"""
    if MAPPINGS_FILE.exists():
        with open(MAPPINGS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def detect_website_type(prompt: str) -> Optional[str]:
    """Detect website type from user prompt using enhanced keyword matching"""
    prompt_lower = prompt.lower()

    # Fitness/Gym keywords
    if any(word in prompt_lower for word in ['gym', 'fitness', 'workout', 'training', 'exercise', 'yoga', 'crossfit', 'pilates', 'health club']):
        return 'fitness'

    # Portfolio keywords
    if any(word in prompt_lower for word in ['portfolio', 'designer', 'developer', 'freelance', 'creative', 'personal site', 'showcase']):
        return 'portfolio'

    # SaaS keywords
    if any(word in prompt_lower for word in ['saas', 'software', 'platform', 'dashboard', 'analytics', 'app', 'subscription', 'cloud']):
        return 'saas'

    # Restaurant keywords
    if any(word in prompt_lower for word in ['restaurant', 'cafe', 'food', 'menu', 'dining', 'bistro', 'eatery', 'kitchen']):
        return 'restaurant'

    # E-commerce keywords
    if any(word in prompt_lower for word in ['shop', 'store', 'ecommerce', 'e-commerce', 'product', 'cart', 'buy', 'sell', 'marketplace']):
        return 'ecommerce'

    return None


def load_component_from_library(component_path: str) -> Optional[str]:
    """
    Load a component from the library
    component_path: e.g., "headers/HeaderWithCTA"
    Returns: Component code as string
    """
    file_path = COMPONENTS_DIR / f"{component_path}.jsx"

    if file_path.exists():
        return file_path.read_text(encoding='utf-8')

    return None


def replace_placeholders(content: str, placeholders: Dict[str, str]) -> str:
    """
    Replace {{PLACEHOLDER}} tokens in content with actual values
    Example: {{BRAND_NAME}} -> "FitLife Gym"
    """
    for key, value in placeholders.items():
        content = content.replace(f"{{{{{key}}}}}", value)

    return content


def load_template_components(website_type: str) -> Dict[str, str]:
    """
    Load components for a website type using the mapping system
    Returns: {component_name: component_code}
    Zero tokens used - just file I/O and placeholder replacement
    """
    mappings = load_mappings()

    if website_type not in mappings:
        return {}

    config = mappings[website_type]
    component_paths = config.get("components", [])
    placeholders = config.get("placeholders", {})

    components = {}

    for component_path in component_paths:
        # Load component from library
        component_code = load_component_from_library(component_path)

        if component_code:
            # Replace placeholders with actual values
            component_code = replace_placeholders(component_code, placeholders)

            # Extract component name from path (e.g., "headers/HeaderWithCTA" -> "Header")
            # All components export a default function with a generic name (Header, Hero, etc.)
            # We'll use the last part before the variant name as the component name
            component_name = component_path.split('/')[-1]  # "HeaderWithCTA"

            # Simplify to base name (Header, Hero, Footer, etc.)
            if component_name.startswith('Header'):
                simplified_name = 'Header'
            elif component_name.startswith('Hero'):
                simplified_name = 'Hero'
            elif component_name.startswith('Features'):
                simplified_name = 'Features'
            elif component_name.startswith('Pricing'):
                simplified_name = 'Pricing'
            elif component_name.startswith('Testimonials'):
                simplified_name = 'Testimonials'
            elif component_name.startswith('Footer'):
                simplified_name = 'Footer'
            else:
                simplified_name = component_name

            components[simplified_name] = component_code

    return components


def load_template_css(website_type: str) -> Optional[str]:
    """
    Load CSS for a website type using the mapping system
    Returns: Complete CSS code
    Zero tokens used - just file I/O
    """
    mappings = load_mappings()

    if website_type not in mappings:
        return None

    config = mappings[website_type]
    style_name = config.get("style", "modern")

    css_path = STYLES_DIR / f"{style_name}.css"

    if css_path.exists():
        return css_path.read_text(encoding='utf-8')

    return None


def get_template_data(website_type: str) -> Dict:
    """
    Get all template data for a website type
    Returns components list and loaded files using the mapping system
    """
    if not website_type:
        return {}

    components = load_template_components(website_type)
    css = load_template_css(website_type)

    if not components:
        return {}

    return {
        "components": list(components.keys()),  # ["Header", "Hero", "Features", ...]
        "files": components,  # {"Header": "complete jsx code", ...}
        "css": css  # "complete css code"
    }


def get_available_website_types() -> List[str]:
    """Get list of available website types from mappings"""
    mappings = load_mappings()
    return list(mappings.keys())


def get_component_info(website_type: str) -> Dict:
    """Get information about components for a website type"""
    mappings = load_mappings()

    if website_type not in mappings:
        return {}

    config = mappings[website_type]

    return {
        "type": website_type,
        "components": config.get("components", []),
        "style": config.get("style", "modern"),
        "placeholders": list(config.get("placeholders", {}).keys())
    }
