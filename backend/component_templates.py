"""
Static Template System - Loads complete, production-ready components from disk
Zero tokens used for structure - only content customization if needed
"""

from pathlib import Path
from typing import Dict, Optional

TEMPLATES_DIR = Path(__file__).parent / "templates"


def detect_website_type(prompt: str) -> Optional[str]:
    """Detect website type from user prompt"""
    prompt_lower = prompt.lower()

    # Fitness/Gym keywords
    if any(word in prompt_lower for word in ['gym', 'fitness', 'workout', 'training', 'exercise', 'yoga', 'crossfit', 'pilates']):
        return 'fitness'

    # E-commerce keywords (future)
    # if any(word in prompt_lower for word in ['shop', 'store', 'ecommerce', 'e-commerce', 'product', 'cart']):
    #     return 'ecommerce'

    # Restaurant keywords (future)
    # if any(word in prompt_lower for word in ['restaurant', 'cafe', 'food', 'menu', 'dining']):
    #     return 'restaurant'

    return None


def load_template_components(website_type: str) -> Dict[str, str]:
    """
    Load complete component files from disk
    Returns: {component_name: file_content}
    Zero tokens used - just file I/O
    """
    template_path = TEMPLATES_DIR / website_type

    if not template_path.exists():
        return {}

    components = {}
    components_dir = template_path / "components"

    if components_dir.exists():
        for component_file in components_dir.glob("*.jsx"):
            component_name = component_file.stem  # e.g., "Header" from "Header.jsx"
            components[component_name] = component_file.read_text(encoding='utf-8')

    return components


def load_template_css(website_type: str) -> Optional[str]:
    """
    Load complete CSS file from disk
    Zero tokens used - just file I/O
    """
    css_path = TEMPLATES_DIR / website_type / "App.css"

    if css_path.exists():
        return css_path.read_text(encoding='utf-8')

    return None


def get_template_data(website_type: str) -> Dict:
    """
    Get all template data for a website type
    Returns components list and loaded files
    """
    if not website_type:
        return {}

    components = load_template_components(website_type)
    css = load_template_css(website_type)

    if not components:
        return {}

    return {
        "components": list(components.keys()),  # ["Header", "Hero", "Services", ...]
        "files": components,  # {"Header": "complete jsx code", ...}
        "css": css  # "complete css code"
    }
