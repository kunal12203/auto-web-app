#!/usr/bin/env python3
"""
Test Intent-Based Template Selection System
Demonstrates the complete flow without requiring actual template catalog
"""

import logging
from intent_classifier import classify_prompt
from template_metadata_schema import (
    TemplateCatalog,
    TemplateMetadata,
    IntentInfo,
    Features,
    TechnicalInfo,
    QualityMetrics,
    Relationships
)
from template_matcher import TemplateMatcher
from composition_validator import CompositionValidator
from template_selection_engine import TemplateSelectionEngine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_mock_catalog() -> TemplateCatalog:
    """Create a small mock catalog for testing"""
    catalog = TemplateCatalog()

    # Add some example templates
    templates = [
        # Headers
        TemplateMetadata(
            id="nav_header_headerwithcta_001",
            name="HeaderWithCTA",
            display_name="Header With CTA",
            description="Modern header with navigation and CTA button",
            intent=IntentInfo(domain="navigation", category="header", intent="header", variant="with_cta"),
            features=Features(has=["logo", "navigation_links", "cta_button", "mobile_menu"]),
            use_cases=["saas", "landing_page"],
            technical=TechnicalInfo(framework="react", dependencies=["react", "react-icons"]),
            quality_metrics=QualityMetrics(usage_count=1200, user_rating=4.8),
            keywords=["header", "navbar", "navigation", "cta"],
            file_path="templates/components/headers/HeaderWithCTA.jsx"
        ),

        TemplateMetadata(
            id="nav_header_headerminimal_002",
            name="HeaderMinimal",
            display_name="Header Minimal",
            description="Minimal header with logo and simple navigation",
            intent=IntentInfo(domain="navigation", category="header", intent="header", variant="minimal"),
            features=Features(has=["logo", "navigation_links"]),
            use_cases=["portfolio", "blog"],
            technical=TechnicalInfo(framework="react"),
            quality_metrics=QualityMetrics(usage_count=800, user_rating=4.6),
            keywords=["header", "navbar", "minimal", "simple"],
            file_path="templates/components/headers/HeaderMinimal.jsx"
        ),

        # Heroes
        TemplateMetadata(
            id="landing_hero_herogradient_003",
            name="HeroGradient",
            display_name="Hero Gradient",
            description="Hero section with gradient background",
            intent=IntentInfo(domain="landing", category="hero", intent="hero", variant="gradient"),
            features=Features(has=["headline", "subheadline", "cta_button", "animated"]),
            use_cases=["saas", "landing_page"],
            technical=TechnicalInfo(framework="react"),
            quality_metrics=QualityMetrics(usage_count=1500, user_rating=4.9),
            relationships=Relationships(pairs_well_with=["HeaderWithCTA", "PricingTable"]),
            keywords=["hero", "banner", "gradient"],
            file_path="templates/components/heroes/HeroGradient.jsx"
        ),

        # Pricing
        TemplateMetadata(
            id="pricing_table_pricingtabletoggle_004",
            name="PricingTableToggle",
            display_name="Pricing Table With Toggle",
            description="Pricing table with monthly/annual toggle",
            intent=IntentInfo(domain="pricing", category="table", intent="table", variant="toggle"),
            features=Features(has=["pricing_tiers", "toggle", "features_list", "cta_buttons"]),
            use_cases=["saas"],
            technical=TechnicalInfo(framework="react"),
            quality_metrics=QualityMetrics(usage_count=2000, user_rating=4.9),
            keywords=["pricing", "subscription", "toggle"],
            file_path="templates/components/pricing/PricingTableToggle.jsx"
        ),

        # Testimonials
        TemplateMetadata(
            id="content_testimonials_testimonialscarousel_005",
            name="TestimonialsCarousel",
            display_name="Testimonials Carousel",
            description="Rotating testimonials carousel",
            intent=IntentInfo(domain="content", category="testimonials", intent="testimonials", variant="carousel"),
            features=Features(has=["testimonial_items", "carousel", "author_info", "images"]),
            use_cases=["saas", "ecommerce"],
            technical=TechnicalInfo(framework="react", dependencies=["react", "swiper"]),
            quality_metrics=QualityMetrics(usage_count=900, user_rating=4.7),
            keywords=["testimonials", "reviews", "carousel"],
            file_path="templates/components/testimonials/TestimonialsCarousel.jsx"
        ),

        # Footer
        TemplateMetadata(
            id="nav_footer_footernewsletter_006",
            name="FooterNewsletter",
            display_name="Footer With Newsletter",
            description="Footer with newsletter signup",
            intent=IntentInfo(domain="navigation", category="footer", intent="footer", variant="newsletter"),
            features=Features(has=["links", "newsletter_signup", "social_links"]),
            use_cases=["saas", "landing_page"],
            technical=TechnicalInfo(framework="react"),
            quality_metrics=QualityMetrics(usage_count=1100, user_rating=4.6),
            relationships=Relationships(requires=["Header"]),
            keywords=["footer", "newsletter", "subscribe"],
            file_path="templates/components/footers/FooterNewsletter.jsx"
        ),

        # E-commerce
        TemplateMetadata(
            id="ecommerce_cart_cartslideout_007",
            name="CartSlideout",
            display_name="Shopping Cart Slideout",
            description="Slide-out shopping cart panel",
            intent=IntentInfo(domain="ecommerce", category="cart", intent="cart", variant="slideout"),
            features=Features(has=["cart_items", "quantity_selector", "total", "checkout_button"]),
            use_cases=["ecommerce"],
            technical=TechnicalInfo(framework="react"),
            quality_metrics=QualityMetrics(usage_count=1300, user_rating=4.8),
            keywords=["cart", "shopping", "ecommerce"],
            file_path="templates/components/carts/CartSlideout.jsx"
        ),

        # Login
        TemplateMetadata(
            id="auth_login_loginsimple_008",
            name="LoginSimple",
            display_name="Simple Login Form",
            description="Simple email/password login form",
            intent=IntentInfo(domain="authentication", category="login", intent="login", variant="simple"),
            features=Features(has=["email_input", "password_input", "remember_me", "submit_button"]),
            use_cases=["saas", "dashboard"],
            technical=TechnicalInfo(framework="react"),
            quality_metrics=QualityMetrics(usage_count=2500, user_rating=4.7),
            keywords=["login", "signin", "authentication"],
            file_path="templates/components/auth/LoginSimple.jsx"
        ),
    ]

    for template in templates:
        catalog.add_template(template)

    return catalog


def test_intent_classification():
    """Test 1: Intent Classification"""
    logger.info("\n" + "=" * 70)
    logger.info("TEST 1: INTENT CLASSIFICATION")
    logger.info("=" * 70)

    prompts = [
        "Create a login form",
        "Build a SaaS landing page with pricing and testimonials",
        "Create an e-commerce store with shopping cart"
    ]

    for prompt in prompts:
        logger.info(f"\nPrompt: {prompt}")
        intents = classify_prompt(prompt)

        logger.info(f"Found {len(intents)} intents:")
        for intent in intents:
            logger.info(f"  - {intent.get_path()} (confidence: {intent.confidence:.2f})")


def test_template_matching():
    """Test 2: Template Matching"""
    logger.info("\n" + "=" * 70)
    logger.info("TEST 2: TEMPLATE MATCHING")
    logger.info("=" * 70)

    catalog = create_mock_catalog()
    matcher = TemplateMatcher(catalog)

    # Test matching a login intent
    from intent_classifier import Intent

    login_intent = Intent(
        domain="authentication",
        category="login",
        intent="login",
        variant="simple",
        confidence=0.95,
        features=["email_input", "password_input"]
    )

    logger.info(f"\nMatching intent: {login_intent.get_path()}")
    matches = matcher.match(login_intent)

    if matches:
        logger.info(f"Found {len(matches)} matches:")
        for match in matches:
            logger.info(f"  - {match.template.name} (score: {match.score:.1f})")
            logger.info(f"    Reasons: {', '.join(match.match_reasons[:2])}")
    else:
        logger.info("No matches found")


def test_composition_validation():
    """Test 3: Composition Validation"""
    logger.info("\n" + "=" * 70)
    logger.info("TEST 3: COMPOSITION VALIDATION")
    logger.info("=" * 70)

    catalog = create_mock_catalog()
    validator = CompositionValidator(catalog)

    # Test with good composition
    template_ids = [
        "nav_header_headerwithcta_001",
        "landing_hero_herogradient_003",
        "pricing_table_pricingtabletoggle_004",
        "nav_footer_footernewsletter_006"
    ]

    logger.info(f"\nValidating {len(template_ids)} templates...")
    result = validator.validate(template_ids)

    logger.info(f"Valid: {result.valid}")
    logger.info(f"Conflicts: {len(result.conflicts)}")
    logger.info(f"Missing: {len(result.missing)}")
    logger.info(f"Suggestions: {len(result.suggestions)}")

    if result.suggestions:
        logger.info("\nTop suggestions:")
        for suggestion in result.suggestions[:3]:
            logger.info(f"  - {suggestion}")


def test_full_selection():
    """Test 4: Full Selection Engine"""
    logger.info("\n" + "=" * 70)
    logger.info("TEST 4: FULL SELECTION ENGINE")
    logger.info("=" * 70)

    catalog = create_mock_catalog()
    engine = TemplateSelectionEngine(catalog, use_llm=False)  # Disable LLM for testing

    prompt = "Create a SaaS landing page with pricing and testimonials"

    logger.info(f"\nPrompt: {prompt}")
    logger.info("\nRunning full selection...\n")

    result = engine.select_templates(prompt, website_type="saas")

    logger.info("\n" + "=" * 70)
    logger.info("RESULTS")
    logger.info("=" * 70)
    logger.info(f"Selected Templates: {len(result.selected_templates)}")
    logger.info(f"Quality Score: {result.quality_score:.1f}/100")
    logger.info(f"Validation: {'✅ PASS' if result.validation.valid else '❌ FAIL'}")

    logger.info("\nSelected Templates:")
    for intent_path, explanation in result.explanations.items():
        logger.info(f"  {intent_path}:")
        logger.info(f"    → {explanation.selected_template_name}")
        logger.info(f"       Score: {explanation.score:.1f}, Confidence: {explanation.confidence:.2f}")
        if explanation.reasons:
            logger.info(f"       Reason: {explanation.reasons[0]}")

    # Print full explanation
    logger.info("\n" + engine.explain_selection(result, detailed=True))


def main():
    """Run all tests"""
    logger.info("🧪 INTENT-BASED TEMPLATE SELECTION - TEST SUITE")

    try:
        test_intent_classification()
        test_template_matching()
        test_composition_validation()
        test_full_selection()

        logger.info("\n" + "=" * 70)
        logger.info("✅ ALL TESTS COMPLETED SUCCESSFULLY")
        logger.info("=" * 70)
        logger.info("\nNext steps:")
        logger.info("1. Run: python generate_template_metadata.py")
        logger.info("2. This will create template_catalog.json with all 2,200 templates")
        logger.info("3. Then use the selection engine with real templates!")

    except Exception as e:
        logger.error(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == '__main__':
    exit(main())
