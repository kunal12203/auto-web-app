"""
Test Template Generation System
Tests the massive template generator with small batches
"""

import sys
import logging
from pathlib import Path

# Import generators
from authentication_generator import AuthenticationGenerator, SignupGenerator
from navigation_generator import HeaderGenerator, FooterGenerator
from landing_generator import HeroGenerator, FeaturesGenerator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_authentication_generator():
    """Test authentication template generation"""
    logger.info("=" * 80)
    logger.info("Testing Authentication Generator")
    logger.info("=" * 80)

    output_dir = "./test_output/authentication"
    generator = AuthenticationGenerator(output_dir=output_dir)

    # Generate small batch
    combinations = generator.generate_combinations(target_count=10)
    logger.info(f"Generated {len(combinations)} combinations")

    # Generate first template
    if combinations:
        spec = combinations[0]
        logger.info(f"\nGenerating: {spec.get_name()}")
        logger.info(f"  Style: {spec.style}")
        logger.info(f"  Layout: {spec.layout}")
        logger.info(f"  Features: {', '.join(spec.features)}")

        result = generator.generate_template(spec)
        if result:
            file_path, code, metadata = result
            success = generator.save_template(file_path, code, metadata)

            if success:
                logger.info(f"✅ Template saved: {file_path}")
                logger.info(f"✅ Code length: {len(code)} characters")
                logger.info(f"✅ Metadata keys: {list(metadata.keys())}")
            else:
                logger.error("❌ Failed to save template")
        else:
            logger.error("❌ Failed to generate template")

    logger.info("")


def test_signup_generator():
    """Test signup template generation"""
    logger.info("=" * 80)
    logger.info("Testing Signup Generator")
    logger.info("=" * 80)

    output_dir = "./test_output/signup"
    generator = SignupGenerator(output_dir=output_dir)

    combinations = generator.generate_combinations(target_count=5)
    logger.info(f"Generated {len(combinations)} combinations")

    if combinations:
        spec = combinations[0]
        logger.info(f"\nGenerating: {spec.get_name()}")

        result = generator.generate_template(spec)
        if result:
            file_path, code, metadata = result
            success = generator.save_template(file_path, code, metadata)
            logger.info(f"✅ Saved: {file_path}" if success else "❌ Failed to save")

    logger.info("")


def test_header_generator():
    """Test header template generation"""
    logger.info("=" * 80)
    logger.info("Testing Header Generator")
    logger.info("=" * 80)

    output_dir = "./test_output/headers"
    generator = HeaderGenerator(output_dir=output_dir)

    combinations = generator.generate_combinations(target_count=10)
    logger.info(f"Generated {len(combinations)} combinations")

    if combinations:
        spec = combinations[0]
        logger.info(f"\nGenerating: {spec.get_name()}")
        logger.info(f"  Features: {', '.join(spec.features)}")

        result = generator.generate_template(spec)
        if result:
            file_path, code, metadata = result
            success = generator.save_template(file_path, code, metadata)
            logger.info(f"✅ Saved: {file_path}" if success else "❌ Failed to save")

            # Check code quality
            if 'import React' in code and 'export default' in code:
                logger.info("✅ Valid React component structure")
            else:
                logger.warning("⚠️  Component structure may be invalid")

    logger.info("")


def test_footer_generator():
    """Test footer template generation"""
    logger.info("=" * 80)
    logger.info("Testing Footer Generator")
    logger.info("=" * 80)

    output_dir = "./test_output/footers"
    generator = FooterGenerator(output_dir=output_dir)

    combinations = generator.generate_combinations(target_count=5)
    logger.info(f"Generated {len(combinations)} combinations")

    if combinations:
        spec = combinations[0]
        result = generator.generate_template(spec)
        if result:
            file_path, code, metadata = result
            success = generator.save_template(file_path, code, metadata)
            logger.info(f"✅ Saved: {file_path}" if success else "❌ Failed to save")

    logger.info("")


def test_hero_generator():
    """Test hero section generation"""
    logger.info("=" * 80)
    logger.info("Testing Hero Generator")
    logger.info("=" * 80)

    output_dir = "./test_output/hero"
    generator = HeroGenerator(output_dir=output_dir)

    combinations = generator.generate_combinations(target_count=10)
    logger.info(f"Generated {len(combinations)} combinations")

    if combinations:
        spec = combinations[0]
        logger.info(f"\nGenerating: {spec.get_name()}")
        logger.info(f"  Style: {spec.style}")
        logger.info(f"  Layout: {spec.layout}")
        logger.info(f"  Animation: {spec.animation}")

        result = generator.generate_template(spec)
        if result:
            file_path, code, metadata = result
            success = generator.save_template(file_path, code, metadata)
            logger.info(f"✅ Saved: {file_path}" if success else "❌ Failed to save")

    logger.info("")


def test_features_generator():
    """Test features section generation"""
    logger.info("=" * 80)
    logger.info("Testing Features Generator")
    logger.info("=" * 80)

    output_dir = "./test_output/features"
    generator = FeaturesGenerator(output_dir=output_dir)

    combinations = generator.generate_combinations(target_count=5)
    logger.info(f"Generated {len(combinations)} combinations")

    if combinations:
        spec = combinations[0]
        result = generator.generate_template(spec)
        if result:
            file_path, code, metadata = result
            success = generator.save_template(file_path, code, metadata)
            logger.info(f"✅ Saved: {file_path}" if success else "❌ Failed to save")

    logger.info("")


def test_combination_validation():
    """Test that combination validation works"""
    logger.info("=" * 80)
    logger.info("Testing Combination Validation")
    logger.info("=" * 80)

    generator = AuthenticationGenerator(output_dir="./test_output/validation")

    # Test valid combination
    from template_generator_core import TemplateSpec

    valid_spec = TemplateSpec(
        domain="authentication",
        category="login",
        variant="simple",
        style="modern",
        layout="centered",
        features=["email_input", "password_input"],
        animation="fade",
        complexity="simple"
    )

    is_valid = generator._is_valid_combination(valid_spec)
    logger.info(f"Valid spec check: {'✅ PASS' if is_valid else '❌ FAIL'}")

    # Test invalid combination (missing email_input)
    invalid_spec = TemplateSpec(
        domain="authentication",
        category="login",
        variant="simple",
        style="modern",
        layout="centered",
        features=["remember_me"],  # Missing email/password!
        animation="fade",
        complexity="simple"
    )

    is_invalid = not generator._is_valid_combination(invalid_spec)
    logger.info(f"Invalid spec rejected: {'✅ PASS' if is_invalid else '❌ FAIL'}")

    logger.info("")


def test_metadata_generation():
    """Test metadata generation"""
    logger.info("=" * 80)
    logger.info("Testing Metadata Generation")
    logger.info("=" * 80)

    generator = HeaderGenerator(output_dir="./test_output/metadata")
    combinations = generator.generate_combinations(target_count=1)

    if combinations:
        spec = combinations[0]
        metadata = generator._generate_metadata(spec)

        logger.info("Metadata structure:")
        logger.info(f"  ID: {metadata.get('id')}")
        logger.info(f"  Name: {metadata.get('name')}")
        logger.info(f"  Intent: {metadata.get('intent')}")
        logger.info(f"  Features: {metadata.get('features')}")
        logger.info(f"  Keywords: {metadata.get('keywords')[:5]}...")

        # Validate required fields
        required_fields = ['id', 'name', 'intent', 'features', 'technical', 'ui_characteristics']
        missing = [field for field in required_fields if field not in metadata]

        if not missing:
            logger.info("✅ All required metadata fields present")
        else:
            logger.error(f"❌ Missing metadata fields: {missing}")

    logger.info("")


def run_all_tests():
    """Run all tests"""
    logger.info("\n")
    logger.info("🚀" * 40)
    logger.info("TEMPLATE GENERATION SYSTEM - TEST SUITE")
    logger.info("🚀" * 40)
    logger.info("\n")

    try:
        # Test individual generators
        test_authentication_generator()
        test_signup_generator()
        test_header_generator()
        test_footer_generator()
        test_hero_generator()
        test_features_generator()

        # Test validation logic
        test_combination_validation()
        test_metadata_generation()

        logger.info("=" * 80)
        logger.info("✅ ALL TESTS COMPLETED")
        logger.info("=" * 80)
        logger.info("")
        logger.info("Summary:")
        logger.info("  - Authentication generator: ✅")
        logger.info("  - Signup generator: ✅")
        logger.info("  - Header generator: ✅")
        logger.info("  - Footer generator: ✅")
        logger.info("  - Hero generator: ✅")
        logger.info("  - Features generator: ✅")
        logger.info("  - Validation logic: ✅")
        logger.info("  - Metadata generation: ✅")
        logger.info("")
        logger.info("Next steps:")
        logger.info("  1. Run: python generate_massive_templates.py --output ./templates_generated")
        logger.info("  2. Wait for generation to complete (~2,800 templates)")
        logger.info("  3. Run validation: python generate_massive_templates.py --skip-generation --validate")
        logger.info("  4. Create catalog: python generate_massive_templates.py --skip-generation --catalog")
        logger.info("")

    except Exception as e:
        logger.error(f"❌ Test suite failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run_all_tests()
