"""
Intelligent Hybrid Template + AI System
AI analyzes prompt → Matches with templates → Generates missing components
Maximizes token savings while maintaining flexibility
"""

from pathlib import Path
from typing import Dict, List, Optional, Tuple
import json
from component_templates import (
    load_component_from_library,
    replace_placeholders,
    COMPONENTS_DIR,
    STYLES_DIR,
    load_mappings
)

# Component library catalog with descriptions for AI matching
COMPONENT_CATALOG = {
    "headers/HeaderWithCTA": {
        "description": "Header with navigation, logo, and call-to-action button",
        "keywords": ["header", "navigation", "nav", "menu", "cta", "signup", "login"],
        "type": "Header"
    },
    "headers/HeaderMinimal": {
        "description": "Minimal header with just logo and navigation links",
        "keywords": ["header", "navigation", "nav", "minimal", "simple", "clean"],
        "type": "Header"
    },
    "heroes/HeroImage": {
        "description": "Hero section with headline, description, CTA buttons, and image/icon",
        "keywords": ["hero", "banner", "landing", "headline", "cta", "image"],
        "type": "Hero"
    },
    "heroes/HeroCentered": {
        "description": "Centered hero section with headline, description, and CTA buttons",
        "keywords": ["hero", "banner", "landing", "centered", "headline", "cta"],
        "type": "Hero"
    },
    "heroes/HeroMinimal": {
        "description": "Minimal hero section with headline and single CTA",
        "keywords": ["hero", "banner", "minimal", "simple", "headline"],
        "type": "Hero"
    },
    "features/FeaturesGrid": {
        "description": "Grid layout displaying 4 features/services with icons, titles, and descriptions",
        "keywords": ["features", "services", "benefits", "grid", "what we do", "offerings"],
        "type": "Features"
    },
    "features/FeaturesList": {
        "description": "Vertical list layout displaying features with icons and descriptions",
        "keywords": ["features", "services", "benefits", "list", "vertical"],
        "type": "Features"
    },
    "pricing/PricingCards": {
        "description": "Pricing table with 3 tiers showing plans, prices, and features",
        "keywords": ["pricing", "plans", "subscription", "tiers", "cost", "payment"],
        "type": "Pricing"
    },
    "testimonials/TestimonialsGrid": {
        "description": "Grid of customer testimonials/reviews with quotes and author info",
        "keywords": ["testimonials", "reviews", "feedback", "customers", "quotes"],
        "type": "Testimonials"
    },
    "footers/FooterComprehensive": {
        "description": "Full footer with multiple columns: about, links, contact, social media",
        "keywords": ["footer", "contact", "social", "links", "comprehensive", "full"],
        "type": "Footer"
    },
    "footers/FooterMinimal": {
        "description": "Minimal footer with brand name, tagline, and simple links",
        "keywords": ["footer", "minimal", "simple", "basic"],
        "type": "Footer"
    }
}


def analyze_prompt_for_components(prompt: str, use_ai: bool = True) -> Dict:
    """
    Analyze user prompt to determine which components are needed
    Returns: {
        "website_type": str,
        "project_type": str (simple/react/fullstack),
        "components_needed": List[str],
        "special_features": List[str]
    }
    """
    prompt_lower = prompt.lower()

    # Detect project type from prompt
    project_type = "react"  # default
    if any(word in prompt_lower for word in ['simple', 'html', 'basic', 'static']):
        project_type = "simple"
    elif any(word in prompt_lower for word in ['full stack', 'fullstack', 'backend', 'database', 'api']):
        project_type = "fullstack"

    # Detect website type
    website_type = detect_website_type_intelligent(prompt)

    # Use AI for intelligent component detection (minimal tokens)
    if use_ai:
        components_needed = detect_components_with_ai(prompt)
    else:
        # Fallback: basic keyword matching
        components_needed = detect_components_basic(prompt)

    # Detect special features that might need custom components
    special_features = detect_special_features(prompt)

    return {
        "website_type": website_type,
        "project_type": project_type,
        "components_needed": components_needed,
        "special_features": special_features
    }


def detect_website_type_intelligent(prompt: str) -> str:
    """Enhanced website type detection"""
    prompt_lower = prompt.lower()

    # Fitness/Gym
    if any(word in prompt_lower for word in ['gym', 'fitness', 'workout', 'training', 'exercise', 'yoga', 'crossfit', 'pilates', 'health club']):
        return 'fitness'

    # Portfolio
    if any(word in prompt_lower for word in ['portfolio', 'designer', 'developer', 'freelance', 'creative', 'personal site', 'showcase', 'work']):
        return 'portfolio'

    # SaaS
    if any(word in prompt_lower for word in ['saas', 'software', 'platform', 'dashboard', 'analytics', 'app', 'subscription', 'cloud', 'tool']):
        return 'saas'

    # Restaurant/Cafe
    if any(word in prompt_lower for word in ['restaurant', 'cafe', 'coffee', 'food', 'menu', 'dining', 'bistro', 'eatery', 'kitchen', 'bar']):
        return 'restaurant'

    # E-commerce
    if any(word in prompt_lower for word in ['shop', 'store', 'ecommerce', 'e-commerce', 'product', 'cart', 'buy', 'sell', 'marketplace', 'retail']):
        return 'ecommerce'

    # Business/Corporate
    if any(word in prompt_lower for word in ['business', 'corporate', 'company', 'agency', 'consulting', 'professional']):
        return 'business'

    return 'general'


def detect_components_basic(prompt: str) -> List[str]:
    """Basic keyword-based component detection (fallback, no AI)"""
    prompt_lower = prompt.lower()
    components = []

    # Always need header
    components.append("Header")

    # Hero/Landing
    if any(word in prompt_lower for word in ['hero', 'landing', 'banner', 'homepage']):
        components.append("Hero")

    # Features/Services
    if any(word in prompt_lower for word in ['features', 'services', 'offerings', 'benefits', 'what we do']):
        components.append("Features")

    # Pricing
    if any(word in prompt_lower for word in ['pricing', 'plans', 'subscription', 'cost', 'payment']):
        components.append("Pricing")

    # Testimonials
    if any(word in prompt_lower for word in ['testimonial', 'review', 'feedback', 'customer', 'client']):
        components.append("Testimonials")

    # Contact
    if any(word in prompt_lower for word in ['contact', 'get in touch', 'reach us']):
        components.append("Contact")

    # Always need footer
    components.append("Footer")

    return components


def detect_components_with_ai(prompt: str) -> List[str]:
    """
    Use AI to intelligently detect which components are needed
    This is a lightweight AI call (< 500 tokens) just for component analysis
    """
    # For now, use basic detection
    # We'll integrate with Claude API in the main file
    return detect_components_basic(prompt)


def detect_special_features(prompt: str) -> List[str]:
    """Detect special features that need custom AI-generated components"""
    prompt_lower = prompt.lower()
    special = []

    if any(word in prompt_lower for word in ['booking', 'reservation', 'appointment', 'schedule']):
        special.append("BookingSystem")

    if any(word in prompt_lower for word in ['order', 'ordering', 'cart', 'checkout', 'buy online']):
        special.append("OrderingSystem")

    if any(word in prompt_lower for word in ['gallery', 'photos', 'images', 'portfolio grid']):
        special.append("Gallery")

    if any(word in prompt_lower for word in ['blog', 'articles', 'posts', 'news']):
        special.append("Blog")

    if any(word in prompt_lower for word in ['login', 'signup', 'authentication', 'user account']):
        special.append("AuthSystem")

    if any(word in prompt_lower for word in ['search', 'filter', 'find']):
        special.append("SearchFilter")

    if any(word in prompt_lower for word in ['map', 'location', 'directions']):
        special.append("Map")

    return special


def match_components_with_templates(components_needed: List[str], website_type: str) -> Tuple[Dict[str, str], List[str]]:
    """
    Match needed components with available templates
    Returns: (matched_components, components_to_generate)

    matched_components: {component_name: template_path}
    components_to_generate: [component_names]
    """
    matched = {}
    to_generate = []

    # Load website type defaults
    mappings = load_mappings()
    default_placeholders = {}

    if website_type in mappings:
        default_placeholders = mappings[website_type].get("placeholders", {})

    for component in components_needed:
        # Try to find a matching template
        template_path = find_best_template_match(component, website_type)

        if template_path:
            matched[component] = template_path
        else:
            to_generate.append(component)

    return matched, to_generate, default_placeholders


def find_best_template_match(component_name: str, website_type: str) -> Optional[str]:
    """
    Find the best template match for a component
    Returns template path or None
    """
    component_lower = component_name.lower()

    # Direct matches
    if component_lower == "header":
        # Choose header variant based on website type
        if website_type in ['portfolio']:
            return "headers/HeaderMinimal"
        else:
            return "headers/HeaderWithCTA"

    elif component_lower == "hero":
        if website_type in ['portfolio']:
            return "heroes/HeroMinimal"
        elif website_type in ['saas', 'ecommerce']:
            return "heroes/HeroCentered"
        else:
            return "heroes/HeroImage"

    elif component_lower == "features" or component_lower == "services":
        if website_type in ['portfolio']:
            return "features/FeaturesList"
        else:
            return "features/FeaturesGrid"

    elif component_lower == "pricing":
        return "pricing/PricingCards"

    elif component_lower == "testimonials" or component_lower == "reviews":
        return "testimonials/TestimonialsGrid"

    elif component_lower == "footer":
        if website_type in ['portfolio']:
            return "footers/FooterMinimal"
        else:
            return "footers/FooterComprehensive"

    # No match found - needs AI generation
    return None


def load_matched_components(matched: Dict[str, str], placeholders: Dict[str, str]) -> Dict[str, str]:
    """
    Load matched components from templates and replace placeholders
    Returns: {component_name: component_code}
    """
    loaded = {}

    for component_name, template_path in matched.items():
        component_code = load_component_from_library(template_path)

        if component_code:
            # Replace placeholders
            component_code = replace_placeholders(component_code, placeholders)
            loaded[component_name] = component_code

    return loaded


def get_style_for_website_type(website_type: str) -> str:
    """Get the appropriate CSS style for a website type"""
    mappings = load_mappings()

    if website_type in mappings:
        return mappings[website_type].get("style", "modern")

    # Defaults
    style_map = {
        'portfolio': 'minimal',
        'saas': 'professional',
        'business': 'professional',
        'fitness': 'modern',
        'restaurant': 'modern',
        'ecommerce': 'professional'
    }

    return style_map.get(website_type, 'modern')


def load_css_for_style(style_name: str) -> Optional[str]:
    """Load CSS file for a style variant"""
    css_path = STYLES_DIR / f"{style_name}.css"

    if css_path.exists():
        return css_path.read_text(encoding='utf-8')

    return None


def get_template_component_count() -> int:
    """Get total number of available template components"""
    return len(COMPONENT_CATALOG)


def get_component_catalog_summary() -> str:
    """Get a summary of available components for AI context"""
    summary_lines = []

    for path, info in COMPONENT_CATALOG.items():
        summary_lines.append(f"- {info['type']}: {info['description']}")

    return "\n".join(summary_lines)
