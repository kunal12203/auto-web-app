#!/usr/bin/env python3
"""
Template Metadata Generator - Auto-generates metadata for 2,200+ templates
Analyzes file paths and code to create rich metadata for intent-based matching
"""

import os
import re
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from datetime import datetime

from template_metadata_schema import (
    TemplateMetadata,
    IntentInfo,
    Features,
    TechnicalInfo,
    UICharacteristics,
    Relationships,
    QualityMetrics,
    TemplateCatalog
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================================
# METADATA GENERATOR
# ============================================================================

class MetadataGenerator:
    """
    Auto-generates metadata for templates by analyzing:
    1. File paths (to infer intent)
    2. Code content (to extract features, dependencies)
    3. File structure (to detect framework)
    """

    def __init__(self, templates_root: str):
        """
        Args:
            templates_root: Root directory containing all templates
        """
        self.templates_root = Path(templates_root)
        self.generated_count = 0

    def generate_for_all_templates(self) -> TemplateCatalog:
        """
        Generate metadata for all templates in templates_root

        Returns:
            TemplateCatalog with all generated metadata
        """
        logger.info("=" * 70)
        logger.info("TEMPLATE METADATA GENERATOR")
        logger.info("=" * 70)
        logger.info(f"Templates Root: {self.templates_root}")

        catalog = TemplateCatalog()

        # Find all template files
        template_files = self._find_template_files()

        logger.info(f"\nFound {len(template_files)} template files")

        # Generate metadata for each
        for template_file in template_files:
            try:
                metadata = self.generate_metadata(template_file)
                catalog.add_template(metadata)
                self.generated_count += 1

                if self.generated_count % 100 == 0:
                    logger.info(f"  Generated {self.generated_count} / {len(template_files)}...")

            except Exception as e:
                logger.error(f"  ❌ Failed to generate metadata for {template_file}: {e}")

        logger.info(f"\n✅ Generated metadata for {self.generated_count} templates")

        # Print statistics
        stats = catalog.get_stats()
        logger.info("\nCatalog Statistics:")
        logger.info(f"  Total templates: {stats['total_templates']}")
        logger.info(f"  By domain: {stats['by_domain']}")
        logger.info(f"  By framework: {stats['by_framework']}")

        return catalog

    def generate_metadata(self, template_file: Path) -> TemplateMetadata:
        """
        Generate metadata for a single template file

        Args:
            template_file: Path to template file

        Returns:
            TemplateMetadata object
        """
        # Read file content
        code = template_file.read_text()

        # 1. Infer intent from file path
        intent = self._infer_intent_from_path(template_file)

        # 2. Generate ID and names
        template_id = self._generate_id(template_file, intent)
        name = self._extract_component_name(template_file, code)
        display_name = self._generate_display_name(name)

        # 3. Generate description
        description = self._generate_description(name, intent, template_file)

        # 4. Extract features from code
        features = self._extract_features(code, name)

        # 5. Infer use cases from path and content
        use_cases = self._infer_use_cases(template_file, code, intent)

        # 6. Extract technical info
        technical = self._extract_technical_info(code, template_file)

        # 7. Infer UI characteristics
        ui_characteristics = self._infer_ui_characteristics(code, name)

        # 8. Generate keywords
        keywords = self._generate_keywords(name, intent, template_file)

        # 9. Initialize relationships (will be enriched later)
        relationships = Relationships()

        # 10. Initialize quality metrics
        quality_metrics = QualityMetrics(
            usage_count=0,
            user_rating=4.5,  # Default optimistic rating
            completion_rate=0.85,  # Default
            last_updated=datetime.now().isoformat()
        )

        # Create metadata
        metadata = TemplateMetadata(
            id=template_id,
            name=name,
            display_name=display_name,
            description=description,
            intent=intent,
            features=features,
            use_cases=use_cases,
            technical=technical,
            ui_characteristics=ui_characteristics,
            relationships=relationships,
            quality_metrics=quality_metrics,
            keywords=keywords,
            file_path=str(template_file.relative_to(self.templates_root.parent))
        )

        return metadata

    def _find_template_files(self) -> List[Path]:
        """Find all template files"""
        template_files = []

        # Find React component templates (.jsx)
        template_files.extend(self.templates_root.glob('components/**/*.jsx'))

        # Find backend templates (.js)
        template_files.extend(self.templates_root.glob('backend/**/*.js'))

        # Find database templates (.sql)
        template_files.extend(self.templates_root.glob('database/**/*.sql'))

        return sorted(template_files)

    def _infer_intent_from_path(self, template_file: Path) -> IntentInfo:
        """
        Infer intent from file path

        Examples:
        templates/components/headers/HeaderWithCTA.jsx
          → domain: navigation, category: header, variant: with_cta

        templates/components/pricing/PricingTableToggle.jsx
          → domain: pricing, category: table, variant: toggle
        """
        # Get relative path parts
        rel_path = template_file.relative_to(self.templates_root)
        parts = rel_path.parts

        # Default values
        domain = "general"
        category = "component"
        intent = "component"
        variant = None

        # Try to infer from path
        if len(parts) >= 2:
            category_dir = parts[0]  # e.g., "components", "backend", "database"
            subcategory = parts[1] if len(parts) > 1 else ""  # e.g., "headers", "pricing"

            # Map directory names to domains
            if category_dir == "components":
                # Map subcategory to domain
                domain, category = self._map_component_category(subcategory)
                intent = category

            elif category_dir == "backend":
                domain = self._map_backend_category(subcategory)
                category = subcategory or "api"
                intent = category

            elif category_dir == "database":
                domain = "data"
                category = "database"
                intent = subcategory or "schema"

        # Try to infer variant from filename
        filename = template_file.stem  # Without extension
        variant = self._infer_variant_from_name(filename, category)

        return IntentInfo(
            domain=domain,
            category=category,
            intent=intent,
            variant=variant
        )

    def _map_component_category(self, subcategory: str) -> Tuple[str, str]:
        """Map component subcategory to (domain, category)"""
        mapping = {
            # Navigation
            'headers': ('navigation', 'header'),
            'footers': ('navigation', 'footer'),
            'sidebars': ('navigation', 'sidebar'),
            'breadcrumbs': ('navigation', 'breadcrumbs'),
            'navbars': ('navigation', 'header'),

            # Landing
            'heroes': ('landing', 'hero'),
            'ctas': ('landing', 'cta'),
            'features': ('landing', 'features'),

            # Content
            'blogs': ('content', 'blog'),
            'galleries': ('content', 'gallery'),
            'testimonials': ('content', 'testimonials'),
            'teams': ('content', 'team'),
            'faqs': ('content', 'faq'),

            # Ecommerce
            'products': ('ecommerce', 'product_display'),
            'product-display': ('ecommerce', 'product_display'),
            'carts': ('ecommerce', 'cart'),
            'shopping-cart': ('ecommerce', 'cart'),
            'checkout': ('ecommerce', 'checkout'),
            'wishlist': ('ecommerce', 'wishlist'),
            'filters': ('ecommerce', 'product_filters'),

            # Pricing
            'pricing': ('pricing', 'table'),

            # Forms
            'forms': ('forms', 'contact'),
            'contact': ('forms', 'contact'),
            'newsletter': ('forms', 'newsletter'),
            'search': ('forms', 'search'),
            'booking': ('forms', 'booking'),

            # Auth
            'auth': ('authentication', 'login'),
            'login': ('authentication', 'login'),
            'signup': ('authentication', 'signup'),

            # Data
            'tables': ('data', 'table'),
            'charts': ('data', 'charts'),
            'stats': ('data', 'stats'),

            # Admin
            'dashboard': ('admin', 'dashboard'),
            'dashboards': ('admin', 'dashboard'),

            # Overlays
            'modals': ('overlays', 'modal'),
            'toasts': ('overlays', 'toast'),
            'tooltips': ('overlays', 'tooltip'),

            # Feedback
            'loaders': ('feedback', 'loader'),
            'loading': ('feedback', 'loader'),
            'empty-state': ('feedback', 'empty_state'),
        }

        return mapping.get(subcategory.lower(), ('general', subcategory))

    def _map_backend_category(self, subcategory: str) -> str:
        """Map backend subcategory to domain"""
        if 'auth' in subcategory.lower():
            return 'authentication'
        elif any(kw in subcategory.lower() for kw in ['api', 'rest', 'graphql']):
            return 'api'
        elif any(kw in subcategory.lower() for kw in ['database', 'db', 'orm']):
            return 'data'
        else:
            return 'backend'

    def _infer_variant_from_name(self, filename: str, category: str) -> Optional[str]:
        """Infer variant from filename"""
        name_lower = filename.lower()

        # Common variants
        variants = {
            'simple': 'simple',
            'minimal': 'minimal',
            'basic': 'simple',
            'advanced': 'advanced',
            'with_cta': 'with_cta',
            'withcta': 'with_cta',
            'modal': 'modal',
            'slideout': 'slideout',
            'grid': 'grid',
            'list': 'list',
            'carousel': 'carousel',
            'toggle': 'toggle',
            'wizard': 'wizard',
            'detailed': 'detailed',
        }

        for pattern, variant in variants.items():
            if pattern in name_lower:
                return variant

        return None

    def _generate_id(self, template_file: Path, intent: IntentInfo) -> str:
        """Generate unique template ID"""
        # Use file path hash + name
        name = template_file.stem
        path_str = str(template_file.relative_to(self.templates_root))
        hash_suffix = abs(hash(path_str)) % 1000

        # Format: domain_category_name_hash
        template_id = f"{intent.domain}_{intent.category}_{name}_{hash_suffix:03d}"
        template_id = template_id.lower().replace('-', '_')

        return template_id

    def _extract_component_name(self, template_file: Path, code: str) -> str:
        """Extract component name from file or code"""
        # Try to extract from code
        # React: export default function ComponentName
        match = re.search(r'export\s+default\s+function\s+(\w+)', code)
        if match:
            return match.group(1)

        # React: export default ComponentName
        match = re.search(r'export\s+default\s+(\w+)', code)
        if match:
            return match.group(1)

        # React: const ComponentName =
        match = re.search(r'const\s+(\w+)\s*=', code)
        if match:
            name = match.group(1)
            if name[0].isupper():  # Component names start with uppercase
                return name

        # Fallback to filename
        return template_file.stem

    def _generate_display_name(self, name: str) -> str:
        """Generate display name from component name"""
        # Convert camelCase or PascalCase to Title Case
        # HeaderWithCTA → Header With CTA
        display = re.sub(r'([A-Z])', r' \1', name).strip()
        return display

    def _generate_description(self, name: str, intent: IntentInfo, template_file: Path) -> str:
        """Generate description"""
        # Basic description based on intent
        descriptions = {
            'header': f"{name} - Navigation header component",
            'footer': f"{name} - Page footer component",
            'hero': f"{name} - Hero/banner section",
            'cta': f"{name} - Call-to-action section",
            'features': f"{name} - Feature showcase",
            'testimonials': f"{name} - Customer testimonials",
            'pricing': f"{name} - Pricing table",
            'login': f"{name} - User login form",
            'signup': f"{name} - User registration",
            'cart': f"{name} - Shopping cart",
            'product_display': f"{name} - Product display",
        }

        return descriptions.get(intent.category, f"{name} - {intent.category} component")

    def _extract_features(self, code: str, name: str) -> Features:
        """Extract features from code"""
        has_features = []

        # Common React features
        if 'useState' in code:
            has_features.append('state_management')
        if 'useEffect' in code:
            has_features.append('side_effects')
        if 'useContext' in code:
            has_features.append('context')
        if 'onClick' in code or 'onSubmit' in code:
            has_features.append('interactive')
        if 'href=' in code:
            has_features.append('navigation_links')
        if '<button' in code.lower():
            has_features.append('button')
        if '<form' in code.lower():
            has_features.append('form')
        if '<input' in code.lower():
            has_features.append('input_fields')
        if 'type="email"' in code:
            has_features.append('email_input')
        if 'type="password"' in code:
            has_features.append('password_input')
        if '<img' in code.lower() or'<image' in code.lower():
            has_features.append('images')
        if 'className=' in code or 'class=' in code:
            has_features.append('styled')
        if '@media' in code or 'responsive' in code.lower():
            has_features.append('responsive')
        if 'animation' in code.lower() or 'transition' in code.lower():
            has_features.append('animated')

        # Specific UI elements
        if 'logo' in code.lower():
            has_features.append('logo')
        if 'modal' in code.lower():
            has_features.append('modal')
        if 'dropdown' in code.lower() or 'menu' in code.lower():
            has_features.append('dropdown')
        if 'carousel' in code.lower() or 'slider' in code.lower():
            has_features.append('carousel')
        if 'pagination' in code.lower():
            has_features.append('pagination')
        if 'search' in code.lower():
            has_features.append('search')
        if 'filter' in code.lower():
            has_features.append('filter')

        return Features(
            required=[],
            optional=[],
            has=list(set(has_features))  # Unique
        )

    def _infer_use_cases(self, template_file: Path, code: str, intent: IntentInfo) -> List[str]:
        """Infer use cases from path and content"""
        use_cases = []

        path_str = str(template_file).lower()
        code_lower = code.lower()

        # Detect use case from path or content
        if any(kw in path_str for kw in ['saas', 'software', 'platform']):
            use_cases.append('saas')
        if any(kw in path_str for kw in ['ecommerce', 'shop', 'store']):
            use_cases.append('ecommerce')
        if any(kw in path_str for kw in ['portfolio', 'showcase']):
            use_cases.append('portfolio')
        if any(kw in path_str for kw in ['blog', 'article']):
            use_cases.append('blog')
        if any(kw in path_str for kw in ['landing', 'marketing']):
            use_cases.append('landing_page')
        if any(kw in path_str for kw in ['dashboard', 'admin']):
            use_cases.append('dashboard')
        if any(kw in path_str for kw in ['restaurant', 'food', 'menu']):
            use_cases.append('restaurant')
        if any(kw in path_str for kw in ['fitness', 'gym', 'health']):
            use_cases.append('fitness')

        # Infer from intent
        if intent.domain == 'ecommerce':
            use_cases.append('ecommerce')
        elif intent.domain == 'authentication':
            use_cases.extend(['saas', 'dashboard'])
        elif intent.category == 'pricing':
            use_cases.append('saas')
        elif intent.category == 'hero':
            use_cases.extend(['landing_page', 'marketing'])

        return list(set(use_cases)) if use_cases else ['general']

    def _extract_technical_info(self, code: str, template_file: Path) -> TechnicalInfo:
        """Extract technical information from code"""
        # Detect framework
        framework = 'react'  # Default
        if template_file.suffix == '.jsx':
            framework = 'react'
        elif template_file.suffix == '.vue':
            framework = 'vue'
        elif template_file.suffix == '.html':
            framework = 'html'
        elif template_file.suffix == '.js' and 'templates/backend' in str(template_file):
            framework = 'node'

        # Extract dependencies
        dependencies = []
        import_pattern = r"from\s+['\"]([^'\"./][^'\"]*)['\"]"
        matches = re.findall(import_pattern, code)

        for match in matches:
            # Extract package name (first part before /)
            pkg = match.split('/')[0]
            if pkg not in ['react', 'react-dom']:  # Exclude core React
                dependencies.append(pkg)

        dependencies = list(set(dependencies))

        # Detect responsive
        responsive = '@media' in code or 'responsive' in code.lower()

        # Detect accessibility
        accessibility = 'basic'
        if 'aria-' in code or 'role=' in code:
            accessibility = 'WCAG_AA'

        # Detect animations
        animations = []
        if 'animation' in code.lower():
            animations.append('css_animation')
        if 'transition' in code.lower():
            animations.append('css_transition')
        if 'framer-motion' in dependencies:
            animations.append('framer_motion')

        return TechnicalInfo(
            framework=framework,
            dependencies=dependencies,
            responsive=responsive,
            accessibility=accessibility,
            animations=animations
        )

    def _infer_ui_characteristics(self, code: str, name: str) -> UICharacteristics:
        """Infer UI characteristics"""
        name_lower = name.lower()
        code_lower = code.lower()

        # Style
        style = 'modern'
        if 'minimal' in name_lower or 'simple' in name_lower:
            style = 'minimal'
        elif 'bold' in name_lower or 'vibrant' in name_lower:
            style = 'bold'
        elif 'classic' in name_lower:
            style = 'classic'

        # Complexity
        complexity = 'medium'
        code_length = len(code)
        if code_length < 500:
            complexity = 'simple'
        elif code_length > 1500:
            complexity = 'complex'

        # Color scheme
        color_scheme = 'customizable'  # Most templates are customizable

        # Layout
        layout = 'vertical'
        if 'grid' in code_lower or 'flex' in code_lower:
            layout = 'grid'
        elif 'horizontal' in code_lower or 'row' in code_lower:
            layout = 'horizontal'

        return UICharacteristics(
            style=style,
            complexity=complexity,
            color_scheme=color_scheme,
            layout=layout
        )

    def _generate_keywords(self, name: str, intent: IntentInfo, template_file: Path) -> List[str]:
        """Generate keywords for search"""
        keywords = set()

        # Add name variations
        keywords.add(name.lower())

        # Add words from name (camelCase split)
        words = re.findall(r'[A-Z][a-z]*', name)
        keywords.update(w.lower() for w in words)

        # Add intent keywords
        keywords.add(intent.domain)
        keywords.add(intent.category)
        keywords.add(intent.intent)
        if intent.variant:
            keywords.add(intent.variant)

        # Add path-based keywords
        path_parts = template_file.parts
        keywords.update(p.lower().replace('-', ' ').replace('_', ' ') for p in path_parts)

        return sorted(list(keywords))


# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    """Main function to generate metadata for all templates"""
    import argparse

    parser = argparse.ArgumentParser(description='Generate template metadata')
    parser.add_argument('--templates-root', default='templates',
                       help='Root directory containing templates')
    parser.add_argument('--output', default='template_catalog.json',
                       help='Output file for catalog')

    args = parser.parse_args()

    # Generate metadata
    generator = MetadataGenerator(args.templates_root)
    catalog = generator.generate_for_all_templates()

    # Save catalog
    logger.info(f"\n💾 Saving catalog to: {args.output}")
    catalog.save_to_file(args.output)

    logger.info(f"✅ Done! Generated metadata for {generator.generated_count} templates")
    logger.info(f"\nTo use the catalog:")
    logger.info(f"  from template_metadata_schema import load_catalog")
    logger.info(f"  catalog = load_catalog('{args.output}')")


if __name__ == '__main__':
    main()
