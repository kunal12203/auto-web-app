"""
Template Metadata Schema - Rich metadata structure for templates
Enables intelligent matching, composition validation, and quality ranking
"""

from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field, asdict
from datetime import datetime
import json


# ============================================================================
# METADATA SCHEMA
# ============================================================================

@dataclass
class IntentInfo:
    """Intent classification for a template"""
    domain: str
    category: str
    intent: str
    variant: Optional[str] = None

    def get_path(self) -> str:
        """Get full intent path"""
        path = f"{self.domain}.{self.category}.{self.intent}"
        if self.variant:
            path += f".{self.variant}"
        return path


@dataclass
class Features:
    """Template features"""
    required: List[str] = field(default_factory=list)  # Must have to use template
    optional: List[str] = field(default_factory=list)  # Nice to have
    has: List[str] = field(default_factory=list)  # Features this template provides


@dataclass
class TechnicalInfo:
    """Technical specifications"""
    framework: str = "react"  # react, html, vue, etc.
    dependencies: List[str] = field(default_factory=list)  # npm packages needed
    responsive: bool = True
    accessibility: str = "WCAG_AA"  # WCAG_AA, WCAG_AAA, basic, none
    animations: List[str] = field(default_factory=list)  # Types of animations used


@dataclass
class UICharacteristics:
    """UI/UX characteristics"""
    style: str = "modern"  # modern, classic, minimal, bold, etc.
    complexity: str = "medium"  # simple, medium, complex
    color_scheme: str = "customizable"  # customizable, light, dark, colorful
    layout: str = "horizontal"  # horizontal, vertical, grid, flexbox


@dataclass
class Relationships:
    """Relationships with other templates"""
    pairs_well_with: List[str] = field(default_factory=list)  # Works well together
    conflicts_with: List[str] = field(default_factory=list)  # Shouldn't use together
    requires: List[str] = field(default_factory=list)  # Required companions
    similar_but_different: Dict[str, str] = field(default_factory=dict)  # Name: why different


@dataclass
class QualityMetrics:
    """Quality and usage metrics"""
    usage_count: int = 0
    user_rating: float = 4.5  # 0.0-5.0
    completion_rate: float = 0.85  # % of users who finish project using this
    last_updated: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class TemplateMetadata:
    """Complete template metadata"""
    # Basic info
    id: str
    name: str
    display_name: str
    description: str

    # Classification
    intent: IntentInfo

    # Features
    features: Features

    # Use cases
    use_cases: List[str] = field(default_factory=list)  # saas, ecommerce, portfolio, etc.

    # Technical
    technical: TechnicalInfo = field(default_factory=TechnicalInfo)

    # UI
    ui_characteristics: UICharacteristics = field(default_factory=UICharacteristics)

    # Relationships
    relationships: Relationships = field(default_factory=Relationships)

    # Quality
    quality_metrics: QualityMetrics = field(default_factory=QualityMetrics)

    # Search
    keywords: List[str] = field(default_factory=list)

    # File location
    file_path: str = ""

    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return asdict(self)

    def to_json(self) -> str:
        """Convert to JSON string"""
        return json.dumps(self.to_dict(), indent=2)

    @classmethod
    def from_dict(cls, data: Dict) -> 'TemplateMetadata':
        """Create from dictionary"""
        # Convert nested dicts to dataclasses
        if 'intent' in data and isinstance(data['intent'], dict):
            data['intent'] = IntentInfo(**data['intent'])

        if 'features' in data and isinstance(data['features'], dict):
            data['features'] = Features(**data['features'])

        if 'technical' in data and isinstance(data['technical'], dict):
            data['technical'] = TechnicalInfo(**data['technical'])

        if 'ui_characteristics' in data and isinstance(data['ui_characteristics'], dict):
            data['ui_characteristics'] = UICharacteristics(**data['ui_characteristics'])

        if 'relationships' in data and isinstance(data['relationships'], dict):
            data['relationships'] = Relationships(**data['relationships'])

        if 'quality_metrics' in data and isinstance(data['quality_metrics'], dict):
            data['quality_metrics'] = QualityMetrics(**data['quality_metrics'])

        return cls(**data)

    @classmethod
    def from_json(cls, json_str: str) -> 'TemplateMetadata':
        """Create from JSON string"""
        data = json.loads(json_str)
        return cls.from_dict(data)


# ============================================================================
# TEMPLATE CATALOG
# ============================================================================

class TemplateCatalog:
    """Manages the template catalog with metadata"""

    def __init__(self):
        self.templates: Dict[str, TemplateMetadata] = {}
        self.intent_index: Dict[str, List[str]] = {}  # intent_path -> [template_ids]
        self.keyword_index: Dict[str, List[str]] = {}  # keyword -> [template_ids]

    def add_template(self, metadata: TemplateMetadata):
        """Add a template to the catalog"""
        self.templates[metadata.id] = metadata

        # Update intent index
        intent_path = metadata.intent.get_path()
        if intent_path not in self.intent_index:
            self.intent_index[intent_path] = []
        self.intent_index[intent_path].append(metadata.id)

        # Update keyword index
        for keyword in metadata.keywords:
            keyword_lower = keyword.lower()
            if keyword_lower not in self.keyword_index:
                self.keyword_index[keyword_lower] = []
            self.keyword_index[keyword_lower].append(metadata.id)

    def get_template(self, template_id: str) -> Optional[TemplateMetadata]:
        """Get template by ID"""
        return self.templates.get(template_id)

    def get_by_intent(self, intent_path: str) -> List[TemplateMetadata]:
        """Get all templates for an intent"""
        template_ids = self.intent_index.get(intent_path, [])
        return [self.templates[tid] for tid in template_ids if tid in self.templates]

    def search_by_keyword(self, keyword: str) -> List[TemplateMetadata]:
        """Search templates by keyword"""
        keyword_lower = keyword.lower()
        template_ids = self.keyword_index.get(keyword_lower, [])
        return [self.templates[tid] for tid in template_ids if tid in self.templates]

    def get_all_templates(self) -> List[TemplateMetadata]:
        """Get all templates"""
        return list(self.templates.values())

    def save_to_file(self, filepath: str):
        """Save catalog to JSON file"""
        data = {
            'templates': {tid: tmpl.to_dict() for tid, tmpl in self.templates.items()},
            'intent_index': self.intent_index,
            'keyword_index': self.keyword_index
        }

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filepath: str):
        """Load catalog from JSON file"""
        with open(filepath, 'r') as f:
            data = json.load(f)

        self.templates = {}
        for tid, tmpl_data in data.get('templates', {}).items():
            self.templates[tid] = TemplateMetadata.from_dict(tmpl_data)

        self.intent_index = data.get('intent_index', {})
        self.keyword_index = data.get('keyword_index', {})

    def get_stats(self) -> Dict:
        """Get catalog statistics"""
        total = len(self.templates)

        # By domain
        by_domain = {}
        for tmpl in self.templates.values():
            domain = tmpl.intent.domain
            by_domain[domain] = by_domain.get(domain, 0) + 1

        # By framework
        by_framework = {}
        for tmpl in self.templates.values():
            framework = tmpl.technical.framework
            by_framework[framework] = by_framework.get(framework, 0) + 1

        # By use case
        by_use_case = {}
        for tmpl in self.templates.values():
            for use_case in tmpl.use_cases:
                by_use_case[use_case] = by_use_case.get(use_case, 0) + 1

        # Average quality
        total_rating = sum(t.quality_metrics.user_rating for t in self.templates.values())
        avg_rating = total_rating / total if total > 0 else 0

        return {
            'total_templates': total,
            'by_domain': by_domain,
            'by_framework': by_framework,
            'by_use_case': by_use_case,
            'average_rating': round(avg_rating, 2),
            'total_intents': len(self.intent_index),
            'total_keywords': len(self.keyword_index)
        }


# ============================================================================
# EXAMPLE METADATA
# ============================================================================

def create_example_metadata() -> TemplateMetadata:
    """Create an example metadata object"""
    return TemplateMetadata(
        id="header_with_cta_001",
        name="HeaderWithCTA",
        display_name="Modern Header with Call-to-Action",
        description="Modern responsive header with logo, navigation links, and prominent CTA button. Includes mobile hamburger menu.",

        intent=IntentInfo(
            domain="navigation",
            category="header",
            intent="header",
            variant="with_cta"
        ),

        features=Features(
            required=[],
            optional=["search_bar", "language_selector", "dark_mode_toggle"],
            has=["logo", "navigation_links", "cta_button", "mobile_menu", "sticky_scroll"]
        ),

        use_cases=["saas", "landing_page", "marketing", "startup"],

        technical=TechnicalInfo(
            framework="react",
            dependencies=["react", "react-icons"],
            responsive=True,
            accessibility="WCAG_AA",
            animations=["fade_in", "sticky_behavior"]
        ),

        ui_characteristics=UICharacteristics(
            style="modern",
            complexity="medium",
            color_scheme="customizable",
            layout="horizontal"
        ),

        relationships=Relationships(
            pairs_well_with=["HeroGradient", "HeroImage", "CTABold"],
            conflicts_with=["HeaderMinimal", "HeaderTransparent"],
            requires=["Footer"],
            similar_but_different={
                "HeaderMinimal": "Minimal has no CTA button",
                "HeaderMegaMenu": "Mega menu has complex dropdown"
            }
        ),

        quality_metrics=QualityMetrics(
            usage_count=1247,
            user_rating=4.8,
            completion_rate=0.92,
            last_updated="2024-11-15T10:00:00"
        ),

        keywords=[
            "header", "navbar", "navigation", "nav", "top bar",
            "call to action", "cta", "menu", "mobile menu"
        ],

        file_path="templates/components/headers/HeaderWithCTA.jsx"
    )


# ============================================================================
# SINGLETON CATALOG
# ============================================================================

_catalog_instance: Optional[TemplateCatalog] = None


def get_catalog() -> TemplateCatalog:
    """Get singleton catalog instance"""
    global _catalog_instance

    if _catalog_instance is None:
        _catalog_instance = TemplateCatalog()

    return _catalog_instance


def load_catalog(filepath: str) -> TemplateCatalog:
    """Load catalog from file"""
    catalog = get_catalog()
    catalog.load_from_file(filepath)
    return catalog
