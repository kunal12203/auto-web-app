"""
Composition Validator - Ensures templates work well together
Validates template compatibility, checks for conflicts, suggests improvements
"""

import logging
from typing import List, Dict, Set, Optional
from dataclasses import dataclass, field

from template_metadata_schema import TemplateMetadata, TemplateCatalog, get_catalog

logger = logging.getLogger(__name__)


# ============================================================================
# VALIDATION RESULT STRUCTURES
# ============================================================================

@dataclass
class Conflict:
    """Represents a conflict between templates"""
    template1_id: str
    template1_name: str
    template2_id: str
    template2_name: str
    reason: str
    severity: str = "error"  # error, warning, info

    def __str__(self) -> str:
        return f"[{self.severity.upper()}] {self.template1_name} ↔ {self.template2_name}: {self.reason}"


@dataclass
class MissingComponent:
    """Represents a missing required component"""
    component_name: str
    required_by: List[str]  # Templates that require it
    reason: str
    priority: str = "required"  # required, recommended, optional

    def __str__(self) -> str:
        return f"[{self.priority.upper()}] {self.component_name}: {self.reason}"


@dataclass
class Suggestion:
    """Represents a suggestion for improvement"""
    template_name: str
    reason: str
    benefit: str
    priority: int = 5  # 1-10, higher = more important

    def __str__(self) -> str:
        return f"{self.template_name}: {self.reason} ({self.benefit})"


@dataclass
class ValidationResult:
    """Complete validation result"""
    valid: bool
    conflicts: List[Conflict] = field(default_factory=list)
    missing: List[MissingComponent] = field(default_factory=list)
    suggestions: List[Suggestion] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def __str__(self) -> str:
        lines = []
        lines.append(f"Validation: {'✅ PASS' if self.valid else '❌ FAIL'}")

        if self.conflicts:
            lines.append(f"\nConflicts ({len(self.conflicts)}):")
            for conflict in self.conflicts:
                lines.append(f"  - {conflict}")

        if self.missing:
            lines.append(f"\nMissing Components ({len(self.missing)}):")
            for missing in self.missing:
                lines.append(f"  - {missing}")

        if self.warnings:
            lines.append(f"\nWarnings ({len(self.warnings)}):")
            for warning in self.warnings:
                lines.append(f"  - {warning}")

        if self.suggestions:
            lines.append(f"\nSuggestions ({len(self.suggestions)}):")
            for suggestion in self.suggestions[:5]:  # Top 5
                lines.append(f"  - {suggestion}")

        return "\n".join(lines)


# ============================================================================
# COMPOSITION VALIDATOR
# ============================================================================

class CompositionValidator:
    """
    Validates that selected templates work well together

    Checks:
    1. No conflicts (e.g., two headers)
    2. All required dependencies present
    3. Templates pair well together
    4. Suggests complementary templates
    """

    def __init__(self, catalog: Optional[TemplateCatalog] = None):
        """
        Args:
            catalog: Template catalog (uses singleton if not provided)
        """
        self.catalog = catalog or get_catalog()

    def validate(
        self,
        selected_template_ids: List[str],
        allow_warnings: bool = True
    ) -> ValidationResult:
        """
        Validate a set of selected templates

        Args:
            selected_template_ids: List of template IDs
            allow_warnings: If False, warnings are treated as errors

        Returns:
            ValidationResult object
        """
        logger.info(f"🔍 Validating {len(selected_template_ids)} templates...")

        result = ValidationResult(valid=True)

        # Get template objects
        templates = []
        for tid in selected_template_ids:
            template = self.catalog.get_template(tid)
            if template:
                templates.append(template)
            else:
                result.warnings.append(f"Template not found: {tid}")

        if not templates:
            result.valid = False
            return result

        # Run validation checks
        conflicts = self._check_conflicts(templates)
        missing = self._check_missing_dependencies(templates)
        suggestions = self._get_suggestions(templates)
        warnings = self._check_compatibility_warnings(templates)

        result.conflicts = conflicts
        result.missing = missing
        result.suggestions = suggestions
        result.warnings.extend(warnings)

        # Determine overall validity
        # Errors make it invalid
        error_conflicts = [c for c in conflicts if c.severity == "error"]
        required_missing = [m for m in missing if m.priority == "required"]

        if error_conflicts or required_missing:
            result.valid = False

        # Warnings can make it invalid if allow_warnings is False
        if not allow_warnings and (warnings or [c for c in conflicts if c.severity == "warning"]):
            result.valid = False

        logger.info(f"{'✅' if result.valid else '❌'} Validation {'passed' if result.valid else 'failed'}")
        if conflicts:
            logger.warning(f"   Found {len(conflicts)} conflicts")
        if missing:
            logger.warning(f"   Found {len(missing)} missing components")
        if suggestions:
            logger.info(f"   Generated {len(suggestions)} suggestions")

        return result

    def _check_conflicts(self, templates: List[TemplateMetadata]) -> List[Conflict]:
        """
        Check for conflicts between templates

        Conflict types:
        1. Duplicate roles (two headers, two footers)
        2. Explicit conflicts (template.relationships.conflicts_with)
        3. Incompatible styles
        """
        conflicts = []

        # Check for duplicate roles
        role_counts: Dict[str, List[str]] = {}

        for template in templates:
            # Role is determined by intent category
            role = f"{template.intent.domain}.{template.intent.category}"

            if role not in role_counts:
                role_counts[role] = []

            role_counts[role].append(template.name)

        # Find duplicates
        for role, template_names in role_counts.items():
            if len(template_names) > 1:
                # Multiple templates for same role
                for i in range(len(template_names)):
                    for j in range(i + 1, len(template_names)):
                        conflicts.append(Conflict(
                            template1_id=template_names[i],
                            template1_name=template_names[i],
                            template2_id=template_names[j],
                            template2_name=template_names[j],
                            reason=f"Both serve the same role ({role})",
                            severity="error"
                        ))

        # Check explicit conflicts
        for i, template1 in enumerate(templates):
            for j, template2 in enumerate(templates):
                if i >= j:
                    continue

                # Check if template1 conflicts with template2
                if template2.name in template1.relationships.conflicts_with:
                    conflicts.append(Conflict(
                        template1_id=template1.id,
                        template1_name=template1.name,
                        template2_id=template2.id,
                        template2_name=template2.name,
                        reason=template1.relationships.similar_but_different.get(
                            template2.name,
                            "Explicitly marked as conflicting"
                        ),
                        severity="error"
                    ))

        # Check style compatibility
        styles = [t.ui_characteristics.style for t in templates]
        unique_styles = set(styles)

        if len(unique_styles) > 2:
            # Too many different styles might clash
            conflicts.append(Conflict(
                template1_id="",
                template1_name="Style Mix",
                template2_id="",
                template2_name="",
                reason=f"Too many different styles: {', '.join(unique_styles)}. Consider using consistent style.",
                severity="warning"
            ))

        return conflicts

    def _check_missing_dependencies(self, templates: List[TemplateMetadata]) -> List[MissingComponent]:
        """
        Check for missing required dependencies

        Every template can specify required companions
        """
        missing = []

        # Collect all required components
        all_requirements: Dict[str, List[str]] = {}  # component_name -> [required_by]

        for template in templates:
            for required in template.relationships.requires:
                if required not in all_requirements:
                    all_requirements[required] = []
                all_requirements[required].append(template.name)

        # Check which requirements are satisfied
        present_names = {t.name for t in templates}

        for required_name, required_by in all_requirements.items():
            if required_name not in present_names:
                missing.append(MissingComponent(
                    component_name=required_name,
                    required_by=required_by,
                    reason=f"Required by: {', '.join(required_by)}",
                    priority="required"
                ))

        # Check for recommended companions
        # E.g., if you have a Header, you probably want a Footer
        has_header = any(t.intent.category == 'header' for t in templates)
        has_footer = any(t.intent.category == 'footer' for t in templates)

        if has_header and not has_footer:
            missing.append(MissingComponent(
                component_name="Footer",
                required_by=["Standard website structure"],
                reason="Most websites have both header and footer",
                priority="recommended"
            ))

        if has_footer and not has_header:
            missing.append(MissingComponent(
                component_name="Header",
                required_by=["Standard website structure"],
                reason="Most websites have both header and footer",
                priority="recommended"
            ))

        # Check for hero section in landing pages
        has_hero = any(t.intent.category == 'hero' for t in templates)
        has_landing_elements = any(
            t.intent.domain == 'landing' or
            t.intent.category in ['pricing', 'testimonials']
            for t in templates
        )

        if has_landing_elements and not has_hero:
            missing.append(MissingComponent(
                component_name="Hero",
                required_by=["Landing page best practices"],
                reason="Landing pages typically start with a hero section",
                priority="recommended"
            ))

        return missing

    def _get_suggestions(self, templates: List[TemplateMetadata]) -> List[Suggestion]:
        """
        Get suggestions for complementary templates

        Based on:
        1. Template.relationships.pairs_well_with
        2. Common patterns (SaaS sites usually have pricing, testimonials, etc.)
        3. Website type conventions
        """
        suggestions = []

        # Collect templates that pair well with selected ones
        pairs_well: Dict[str, Set[str]] = {}  # template_name -> set of templates it's suggested by

        for template in templates:
            for pairs_with in template.relationships.pairs_well_with:
                if pairs_with not in pairs_well:
                    pairs_well[pairs_with] = set()
                pairs_well[pairs_with].add(template.name)

        # Remove already selected templates
        present_names = {t.name for t in templates}

        for suggested_name, suggested_by in pairs_well.items():
            if suggested_name not in present_names:
                suggestions.append(Suggestion(
                    template_name=suggested_name,
                    reason=f"Pairs well with: {', '.join(list(suggested_by)[:3])}",
                    benefit="Enhanced user experience",
                    priority=len(suggested_by)  # More suggestions = higher priority
                ))

        # Pattern-based suggestions
        # If you have pricing, you might want testimonials
        has_pricing = any(t.intent.category == 'table' and t.intent.domain == 'pricing' for t in templates)
        has_testimonials = any(t.intent.category == 'testimonials' for t in templates)

        if has_pricing and not has_testimonials:
            suggestions.append(Suggestion(
                template_name="Testimonials",
                reason="Pricing pages benefit from social proof",
                benefit="Increases conversion rates",
                priority=8
            ))

        # If you have products, you might want filters
        has_products = any(t.intent.category == 'product_display' for t in templates)
        has_filters = any(t.intent.category == 'product_filters' for t in templates)

        if has_products and not has_filters:
            suggestions.append(Suggestion(
                template_name="ProductFilters",
                reason="Product listings benefit from filtering",
                benefit="Improves user experience for browsing",
                priority=7
            ))

        # If you have a blog, you might want search
        has_blog = any(t.intent.category == 'blog' for t in templates)
        has_search = any(t.intent.category == 'search' for t in templates)

        if has_blog and not has_search:
            suggestions.append(Suggestion(
                template_name="SearchBar",
                reason="Blogs benefit from search functionality",
                benefit="Helps users find content",
                priority=6
            ))

        # Sort suggestions by priority (higher first)
        suggestions.sort(key=lambda s: s.priority, reverse=True)

        return suggestions

    def _check_compatibility_warnings(self, templates: List[TemplateMetadata]) -> List[str]:
        """
        Check for compatibility warnings

        Things that aren't errors but might cause issues
        """
        warnings = []

        # Check framework consistency
        frameworks = {t.technical.framework for t in templates}
        if len(frameworks) > 1:
            warnings.append(
                f"Multiple frameworks detected: {', '.join(frameworks)}. "
                "Ensure they're compatible."
            )

        # Check for missing responsive templates
        non_responsive = [t for t in templates if not t.technical.responsive]
        if non_responsive:
            warnings.append(
                f"{len(non_responsive)} templates are not responsive: "
                f"{', '.join(t.name for t in non_responsive[:3])}"
            )

        # Check accessibility
        low_accessibility = [
            t for t in templates
            if t.technical.accessibility not in ['WCAG_AA', 'WCAG_AAA']
        ]
        if low_accessibility:
            warnings.append(
                f"{len(low_accessibility)} templates have limited accessibility. "
                "Consider upgrading for better user experience."
            )

        # Check for too many dependencies
        all_deps = set()
        for template in templates:
            all_deps.update(template.technical.dependencies)

        if len(all_deps) > 20:
            warnings.append(
                f"Project has {len(all_deps)} dependencies. "
                "Consider if all are necessary to reduce bundle size."
            )

        return warnings

    def auto_fix(
        self,
        selected_template_ids: List[str],
        max_additions: int = 5
    ) -> List[str]:
        """
        Attempt to auto-fix validation issues

        Returns:
            Updated list of template IDs with fixes applied
        """
        logger.info("🔧 Attempting auto-fix...")

        templates = [self.catalog.get_template(tid) for tid in selected_template_ids if self.catalog.get_template(tid)]
        result = self.validate(selected_template_ids)

        fixed_ids = selected_template_ids.copy()

        # Fix missing required components
        additions = 0
        for missing in result.missing:
            if missing.priority == "required" and additions < max_additions:
                # Try to find the required component
                # Search by name
                for template in self.catalog.get_all_templates():
                    if template.name == missing.component_name:
                        fixed_ids.append(template.id)
                        logger.info(f"   ✅ Added missing required component: {missing.component_name}")
                        additions += 1
                        break

        # Remove conflicts (keep higher quality one)
        for conflict in result.conflicts:
            if conflict.severity == "error":
                # Find the templates
                t1 = self.catalog.get_template(conflict.template1_id)
                t2 = self.catalog.get_template(conflict.template2_id)

                if t1 and t2:
                    # Keep the higher quality one
                    if t1.quality_metrics.user_rating >= t2.quality_metrics.user_rating:
                        # Remove t2
                        if conflict.template2_id in fixed_ids:
                            fixed_ids.remove(conflict.template2_id)
                            logger.info(f"   ✅ Removed {conflict.template2_name} (conflict with {conflict.template1_name})")
                    else:
                        # Remove t1
                        if conflict.template1_id in fixed_ids:
                            fixed_ids.remove(conflict.template1_id)
                            logger.info(f"   ✅ Removed {conflict.template1_name} (conflict with {conflict.template2_name})")

        return fixed_ids


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

# Singleton instance
_validator_instance: Optional[CompositionValidator] = None


def get_validator() -> CompositionValidator:
    """Get singleton validator instance"""
    global _validator_instance

    if _validator_instance is None:
        _validator_instance = CompositionValidator()

    return _validator_instance


def validate_templates(template_ids: List[str]) -> ValidationResult:
    """Quick helper to validate templates"""
    validator = get_validator()
    return validator.validate(template_ids)
