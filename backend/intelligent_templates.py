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

# Import the auto-generated catalog of all 202 components
from component_catalog_generated import COMPONENT_CATALOG


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
    Find the best template match for a component using the catalog
    Returns template path or None

    Uses intelligent keyword matching across all 202 components
    """
    component_lower = component_name.lower()

    # Website type preferences for component variants
    TYPE_PREFERENCES = {
        'portfolio': {
            'Header': ['HeaderMinimal', 'HeaderTransparent'],
            'Hero': ['HeroMinimal', 'HeroCentered'],
            'Features': ['FeaturesList', 'FeaturesCompact'],
            'Footer': ['FooterMinimal', 'FooterSimple']
        },
        'saas': {
            'Header': ['HeaderWithCTA', 'HeaderSticky'],
            'Hero': ['HeroCentered', 'HeroWithForm'],
            'Features': ['FeaturesGrid', 'FeaturesWithIcons'],
            'Pricing': ['PricingToggle', 'PricingComparison'],
            'Footer': ['FooterComprehensive', 'FooterMultiColumn']
        },
        'ecommerce': {
            'Header': ['HeaderWithCTA', 'HeaderWithSearch'],
            'Hero': ['HeroSplit', 'HeroImage'],
            'Footer': ['FooterComprehensive', 'FooterMultiColumn']
        },
        'restaurant': {
            'Header': ['HeaderMinimal', 'HeaderCentered'],
            'Hero': ['HeroImage', 'HeroFullscreen'],
            'Footer': ['FooterSocial', 'FooterMinimal']
        },
        'fitness': {
            'Header': ['HeaderWithCTA', 'HeaderTransparent'],
            'Hero': ['HeroVideo', 'HeroFullscreen'],
            'Footer': ['FooterSocial', 'FooterComprehensive']
        },
        'business': {
            'Header': ['HeaderWithCTA', 'HeaderSticky'],
            'Hero': ['HeroCentered', 'HeroSplit'],
            'Footer': ['FooterComprehensive', 'FooterMultiColumn']
        }
    }

    # Step 1: Try to find components by keyword match
    best_match = None
    best_score = 0

    for template_path, info in COMPONENT_CATALOG.items():
        # Calculate match score
        score = 0

        # Check if component type matches
        if info['type'].lower() == component_lower:
            score += 100

        # Check keyword matches
        for keyword in info['keywords']:
            if keyword in component_lower or component_lower in keyword:
                score += 10

        # Bonus for exact keyword match
        if component_lower in info['keywords']:
            score += 50

        # Update best match
        if score > best_score:
            best_score = score
            best_match = template_path

    # Step 2: If we found a match, check if there's a better variant for this website type
    if best_match and best_score >= 100:  # Only if we matched the component type
        component_type = COMPONENT_CATALOG[best_match]['type']

        # Check if we have website-type-specific preferences
        if website_type in TYPE_PREFERENCES and component_type in TYPE_PREFERENCES[website_type]:
            preferred_variants = TYPE_PREFERENCES[website_type][component_type]

            # Try to find a preferred variant
            for template_path, info in COMPONENT_CATALOG.items():
                if info['type'] == component_type:
                    component_name_from_path = template_path.split('/')[-1]
                    if component_name_from_path in preferred_variants:
                        return template_path

        return best_match

    # Step 3: Try fuzzy matching for common patterns
    FUZZY_MATCHES = {
        'cta': 'ctas/CTASimple',
        'call to action': 'ctas/CTASimple',
        'newsletter': 'newsletters/NewsletterSimple',
        'subscribe': 'newsletters/NewsletterSimple',
        'contact': 'contacts/ContactForm',
        'faq': 'faqs/FAQAccordion',
        'team': 'teams/TeamGrid',
        'staff': 'teams/TeamGrid',
        'blog': 'blogs/BlogGrid',
        'gallery': 'galleries/GalleryGrid',
        'video': 'videos/VideoEmbed',
        'social': 'social/SocialLinks',
        'stats': 'stats/StatsGrid',
        'timeline': 'timelines/TimelineVertical',
        'logo': 'logos/LogoGridSimple',
        'search': 'search/SearchBar',
        'modal': 'modals/ModalBasic',
        'form': 'forms/FormContact',
        'card': 'cards/CardBasic',
        'alert': 'alerts/AlertInfo'
    }

    for pattern, template in FUZZY_MATCHES.items():
        if pattern in component_lower:
            return template

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
