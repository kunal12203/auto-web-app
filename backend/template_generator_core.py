"""
Template Generation Core - Foundation for massive template generation
Provides base classes, utilities, and variation combination logic
"""

import os
import re
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Any
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from datetime import datetime

logger = logging.getLogger(__name__)


# ============================================================================
# TEMPLATE VARIATION CONFIGURATIONS
# ============================================================================

@dataclass
class VariationConfig:
    """Configuration for template variations"""
    styles: List[str] = field(default_factory=list)
    layouts: List[str] = field(default_factory=list)
    features: List[List[str]] = field(default_factory=list)
    animations: List[str] = field(default_factory=list)
    complexities: List[str] = field(default_factory=list)


@dataclass
class TemplateSpec:
    """Specification for a template to generate"""
    domain: str
    category: str
    variant: str
    style: str
    layout: str
    features: List[str]
    animation: str
    complexity: str

    def get_name(self) -> str:
        """Generate component name from spec"""
        # Convert to PascalCase
        parts = []

        # Add category
        parts.append(self.category.title().replace('_', ''))

        # Add variant
        if self.variant != 'simple':
            parts.append(self.variant.title().replace('_', ''))

        # Add distinctive features if any
        if 'social' in self.features:
            parts.append('Social')
        if '2fa' in self.features or 'two_factor' in self.features:
            parts.append('2FA')

        # Add style if not modern (modern is default)
        if self.style not in ['modern', 'standard']:
            parts.append(self.style.title())

        # Add layout if distinctive
        if self.layout in ['split', 'sidebar', 'fullscreen']:
            parts.append(self.layout.title())

        name = ''.join(parts)
        return name

    def get_id(self) -> str:
        """Generate unique ID"""
        parts = [
            self.domain,
            self.category,
            self.variant,
            self.style,
            self.layout
        ]

        # Add hash of features for uniqueness
        feature_str = '_'.join(sorted(self.features))
        feature_hash = abs(hash(feature_str)) % 1000

        id_str = '_'.join(parts) + f'_{feature_hash:03d}'
        return id_str.lower().replace('-', '_')


# ============================================================================
# BASE TEMPLATE GENERATOR
# ============================================================================

class BaseTemplateGenerator(ABC):
    """
    Abstract base class for template generators

    Each domain/category has a specific generator that extends this
    """

    def __init__(self, output_dir: str, enable_error_handler: bool = True, use_llm_fixes: bool = True):
        """
        Args:
            output_dir: Directory to output generated templates
            enable_error_handler: Enable automatic error detection and fixing
            use_llm_fixes: Allow LLM-based fixes for complex errors (minimal tokens)
        """
        self.output_dir = Path(output_dir)
        self.generated_count = 0
        self.skipped_count = 0
        self.error_count = 0

        # Initialize error handler if enabled
        self.error_handler = None
        if enable_error_handler:
            try:
                from template_error_handler import TemplateErrorHandler
                self.error_handler = TemplateErrorHandler(
                    use_llm_fallback=use_llm_fixes,
                    use_haiku=True  # Always use Haiku for cost efficiency
                )
                logger.info("Error handler enabled (LLM fallback: %s)", use_llm_fixes)
            except ImportError:
                logger.warning("Could not import error handler, continuing without it")
                self.error_handler = None

    @abstractmethod
    def get_domain(self) -> str:
        """Return domain name"""
        pass

    @abstractmethod
    def get_category(self) -> str:
        """Return category name"""
        pass

    @abstractmethod
    def get_variation_config(self) -> VariationConfig:
        """Return variation configuration"""
        pass

    @abstractmethod
    def generate_code(self, spec: TemplateSpec) -> str:
        """Generate code for template"""
        pass

    def generate_combinations(self, target_count: int) -> List[TemplateSpec]:
        """
        Generate smart combinations of variations

        Args:
            target_count: Target number of templates to generate

        Returns:
            List of TemplateSpec objects
        """
        config = self.get_variation_config()

        # Generate all possible combinations
        all_combinations = []

        for style in config.styles:
            for layout in config.layouts:
                for features in config.features:
                    for animation in config.animations:
                        for complexity in config.complexities:
                            # Determine variant from features
                            variant = self._infer_variant(features)

                            spec = TemplateSpec(
                                domain=self.get_domain(),
                                category=self.get_category(),
                                variant=variant,
                                style=style,
                                layout=layout,
                                features=features,
                                animation=animation,
                                complexity=complexity
                            )

                            # Only add if combination makes sense
                            if self._is_valid_combination(spec):
                                all_combinations.append(spec)

        # Curate to target count
        curated = self._curate_combinations(all_combinations, target_count)

        logger.info(f"Generated {len(all_combinations)} combinations, curated to {len(curated)}")

        return curated

    def _infer_variant(self, features: List[str]) -> str:
        """Infer variant from features"""
        # Override in subclasses for domain-specific logic
        if not features or len(features) <= 2:
            return 'simple'
        elif len(features) <= 4:
            return 'standard'
        else:
            return 'advanced'

    def _is_valid_combination(self, spec: TemplateSpec) -> bool:
        """
        Check if combination is valid

        Override in subclasses for domain-specific validation
        """
        # Some combinations don't make sense
        # e.g., fullscreen + minimal style might be odd

        # Fullscreen is usually not minimal
        if spec.layout == 'fullscreen' and spec.style == 'minimal':
            return False

        # Glassmorphism needs animations usually
        if spec.style == 'glassmorphism' and spec.animation == 'none':
            return False

        return True

    def _curate_combinations(
        self,
        combinations: List[TemplateSpec],
        target_count: int
    ) -> List[TemplateSpec]:
        """
        Curate combinations to target count

        Prioritize diversity and usefulness
        """
        if len(combinations) <= target_count:
            return combinations

        # Score each combination
        scored = []
        for spec in combinations:
            score = self._score_combination(spec)
            scored.append((score, spec))

        # Sort by score descending
        scored.sort(key=lambda x: x[0], reverse=True)

        # Take top target_count
        curated = [spec for _, spec in scored[:target_count]]

        return curated

    def _score_combination(self, spec: TemplateSpec) -> float:
        """
        Score a combination for usefulness

        Higher score = more useful/common
        """
        score = 0.0

        # Prefer common styles
        common_styles = {'modern': 10, 'minimal': 9, 'standard': 8}
        score += common_styles.get(spec.style, 5)

        # Prefer common layouts
        common_layouts = {'centered': 10, 'split': 8, 'card': 7}
        score += common_layouts.get(spec.layout, 5)

        # Prefer moderate complexity
        complexity_scores = {'simple': 8, 'standard': 10, 'advanced': 7}
        score += complexity_scores.get(spec.complexity, 5)

        # Prefer some animation
        if spec.animation != 'none':
            score += 3

        # Prefer useful feature combinations
        if len(spec.features) >= 2 and len(spec.features) <= 5:
            score += 5

        return score

    def generate_template(self, spec: TemplateSpec) -> Optional[Tuple[str, str, Dict]]:
        """
        Generate a complete template with error handling

        Returns:
            (file_path, code, metadata) or None if failed
        """
        try:
            # Generate code
            code = self.generate_code(spec)

            # Validate and fix errors if error handler is available
            if hasattr(self, 'error_handler') and self.error_handler:
                success, fixed_code, messages = self.error_handler.validate_and_fix(
                    code,
                    spec.get_name()
                )

                if success:
                    code = fixed_code
                    if messages:
                        logger.debug(f"Fixed {spec.get_name()}: {', '.join(messages)}")
                else:
                    logger.warning(f"Could not fix all errors in {spec.get_name()}: {', '.join(messages)}")
                    # Continue anyway - let validation catch it later

            # Generate file path
            file_path = self._get_file_path(spec)

            # Generate metadata
            metadata = self._generate_metadata(spec)

            return (str(file_path), code, metadata)

        except Exception as e:
            logger.error(f"Failed to generate template for {spec.get_name()}: {e}")
            self.error_count += 1
            return None

    def _get_file_path(self, spec: TemplateSpec) -> Path:
        """Get output file path for template"""
        # Structure: templates/{domain}/{category}/{ComponentName}.jsx
        domain_dir = self.output_dir / self.get_domain()
        category_dir = domain_dir / self.get_category()

        filename = f"{spec.get_name()}.jsx"

        return category_dir / filename

    def _generate_metadata(self, spec: TemplateSpec) -> Dict:
        """Generate metadata for template"""
        from template_metadata_schema import (
            TemplateMetadata,
            IntentInfo,
            Features,
            TechnicalInfo,
            UICharacteristics,
            QualityMetrics
        )

        intent = IntentInfo(
            domain=spec.domain,
            category=spec.category,
            intent=spec.category,
            variant=spec.variant
        )

        features = Features(
            required=[],
            optional=[],
            has=spec.features.copy()
        )

        technical = TechnicalInfo(
            framework='react',
            dependencies=self._get_dependencies(spec),
            responsive=True,
            accessibility='WCAG_AA',
            animations=[spec.animation] if spec.animation != 'none' else []
        )

        ui = UICharacteristics(
            style=spec.style,
            complexity=spec.complexity,
            color_scheme='customizable',
            layout=spec.layout
        )

        quality = QualityMetrics(
            usage_count=0,
            user_rating=4.5,
            completion_rate=0.85,
            last_updated=datetime.now().isoformat()
        )

        metadata = TemplateMetadata(
            id=spec.get_id(),
            name=spec.get_name(),
            display_name=self._generate_display_name(spec),
            description=self._generate_description(spec),
            intent=intent,
            features=features,
            use_cases=self._infer_use_cases(spec),
            technical=technical,
            ui_characteristics=ui,
            quality_metrics=quality,
            keywords=self._generate_keywords(spec),
            file_path=str(self._get_file_path(spec))
        )

        return metadata.to_dict()

    def _get_dependencies(self, spec: TemplateSpec) -> List[str]:
        """Get npm dependencies for template"""
        deps = ['react']

        # Add icon library if needed
        if any(f in spec.features for f in ['icons', 'social', 'menu']):
            deps.append('react-icons')

        # Add animation library
        if spec.animation in ['scale', 'bounce', 'flip']:
            deps.append('framer-motion')

        return deps

    def _generate_display_name(self, spec: TemplateSpec) -> str:
        """Generate display name"""
        name = spec.get_name()
        # Add spaces before capitals
        display = re.sub(r'([A-Z])', r' \1', name).strip()
        return display

    def _generate_description(self, spec: TemplateSpec) -> str:
        """Generate description"""
        parts = [
            f"{spec.get_name()} -",
            f"{spec.style} style",
            self.get_category(),
            "with" if spec.features else "",
            ', '.join(spec.features[:3]) if spec.features else ""
        ]

        return ' '.join(p for p in parts if p)

    def _infer_use_cases(self, spec: TemplateSpec) -> List[str]:
        """Infer use cases from spec"""
        # Override in subclasses
        return ['general']

    def _generate_keywords(self, spec: TemplateSpec) -> List[str]:
        """Generate keywords for search"""
        keywords = set()

        keywords.add(self.get_category())
        keywords.add(self.get_domain())
        keywords.add(spec.variant)
        keywords.add(spec.style)
        keywords.add(spec.layout)
        keywords.update(spec.features)

        return sorted(list(keywords))

    def save_template(self, file_path: str, code: str, metadata: Dict) -> bool:
        """
        Save template to file

        Returns:
            True if saved successfully
        """
        try:
            # Create directory if needed
            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)

            # Write code
            path.write_text(code)

            # Write metadata
            metadata_path = path.with_suffix('.json')
            metadata_path.write_text(json.dumps(metadata, indent=2))

            self.generated_count += 1
            return True

        except Exception as e:
            logger.error(f"Failed to save template to {file_path}: {e}")
            self.error_count += 1
            return False


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def sanitize_component_name(name: str) -> str:
    """Sanitize component name to be valid JavaScript identifier"""
    # Remove invalid characters
    name = re.sub(r'[^a-zA-Z0-9_]', '', name)

    # Ensure starts with letter
    if name and not name[0].isalpha():
        name = 'Component' + name

    # Ensure PascalCase
    if name and name[0].islower():
        name = name[0].upper() + name[1:]

    return name or 'Component'


def generate_component_imports(features: List[str]) -> str:
    """Generate import statements based on features"""
    imports = ["import React"]

    # Add hooks if needed
    hooks = []
    if any(f in features for f in ['state', 'interactive', 'form']):
        hooks.append('useState')
    if any(f in features for f in ['side_effects', 'animation']):
        hooks.append('useEffect')

    if hooks:
        imports[0] += f", {{ {', '.join(hooks)} }}"

    imports[0] += " from 'react'"

    # Add icons if needed
    if any(f in features for f in ['icons', 'social']):
        imports.append("import { FiMenu, FiX, FiChevronDown } from 'react-icons/fi'")

    return '\n'.join(imports)


def generate_prop_types(features: List[str]) -> str:
    """Generate prop types JSDoc comment"""
    props = []

    if 'onClick' in features or 'interactive' in features:
        props.append(' * @param {Function} onClick - Click handler')
    if 'className' in features:
        props.append(' * @param {string} className - Additional CSS classes')
    if 'children' in features:
        props.append(' * @param {React.ReactNode} children - Child elements')

    if props:
        return '/**\n' + '\n'.join(props) + '\n */'

    return ''
