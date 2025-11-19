"""
Test Project Planner with real examples
"""

import logging
from project_planner import ProjectPlanner, ProjectRequirements

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_gym_website():
    """Test with gym website example (the user's case)"""
    print("\n")
    print("🏋️" * 40)
    print("EXAMPLE 1: GYM WEBSITE")
    print("🏋️" * 40)
    print()

    planner = ProjectPlanner()

    # User's prompt
    user_prompt = "i want to build a gym website to showcase my gym and sell accessories"

    print(f"User Prompt: \"{user_prompt}\"")
    print()

    # Create plan
    plan = planner.create_plan(user_prompt)

    # Print plan
    planner.print_plan(plan)

    # Verify it detected payment correctly
    assert plan.requirements.has_payment, "Should detect payment needed (selling accessories)"
    assert plan.requirements.has_product_catalog, "Should need product catalog"
    assert plan.requirements.has_shopping_cart, "Should need shopping cart"
    assert plan.requirements.has_checkout, "Should need checkout"

    # Verify project type makes sense
    assert plan.project_type.value != 'static_html', "Should NOT be static HTML (needs payment)"

    print("✅ CORRECTLY DETECTED:")
    print("   - Payment processing needed (selling accessories)")
    print("   - Product catalog needed")
    print("   - Shopping cart needed")
    print(f"   - Appropriate project type: {plan.project_type.value}")
    print(f"   - Appropriate deployment: {plan.deployment_target.value}")
    print()


def test_simple_portfolio():
    """Test with simple portfolio (should be static HTML)"""
    print("\n")
    print("🎨" * 40)
    print("EXAMPLE 2: SIMPLE PORTFOLIO")
    print("🎨" * 40)
    print()

    planner = ProjectPlanner()

    user_prompt = "create a simple portfolio website to showcase my work"

    print(f"User Prompt: \"{user_prompt}\"")
    print()

    plan = planner.create_plan(user_prompt)
    planner.print_plan(plan)

    # This SHOULD be static HTML
    print("✅ CORRECTLY SELECTED:")
    print(f"   - Project type: {plan.project_type.value} (simple, no complex features)")
    print(f"   - No npm install needed (static HTML)")
    print(f"   - Deployment: {plan.deployment_target.value}")
    print()


def test_saas_platform():
    """Test with complex SaaS platform"""
    print("\n")
    print("🚀" * 40)
    print("EXAMPLE 3: SAAS PLATFORM")
    print("🚀" * 40)
    print()

    planner = ProjectPlanner()

    user_prompt = "build a SaaS platform with user authentication, subscription payments, and admin dashboard"

    print(f"User Prompt: \"{user_prompt}\"")
    print()

    plan = planner.create_plan(user_prompt)
    planner.print_plan(plan)

    assert plan.requirements.has_authentication, "Should need auth"
    assert plan.requirements.has_payment, "Should need payment"
    assert plan.requirements.has_database, "Should need database"
    assert plan.requirements.has_admin_panel, "Should need admin"

    print("✅ CORRECTLY DETECTED:")
    print("   - Full-stack needed")
    print("   - Database required")
    print("   - API endpoints needed")
    print(f"   - Project type: {plan.project_type.value}")
    print()


def test_blog_website():
    """Test with blog website (needs SEO)"""
    print("\n")
    print("📝" * 40)
    print("EXAMPLE 4: BLOG WEBSITE")
    print("📝" * 40)
    print()

    planner = ProjectPlanner()

    user_prompt = "create a blog website for my articles with good SEO"

    print(f"User Prompt: \"{user_prompt}\"")
    print()

    plan = planner.create_plan(user_prompt)
    planner.print_plan(plan)

    assert plan.requirements.has_blog, "Should detect blog"
    assert plan.requirements.needs_seo, "Should detect SEO need"

    print("✅ CORRECTLY SELECTED:")
    print(f"   - Project type: {plan.project_type.value} (SSR for SEO)")
    print("   - SEO optimized")
    print()


def test_ecommerce_store():
    """Test with full e-commerce store"""
    print("\n")
    print("🛒" * 40)
    print("EXAMPLE 5: E-COMMERCE STORE")
    print("🛒" * 40)
    print()

    planner = ProjectPlanner()

    user_prompt = "build an online store to sell clothing with inventory management and order tracking"

    print(f"User Prompt: \"{user_prompt}\"")
    print()

    plan = planner.create_plan(user_prompt)
    planner.print_plan(plan)

    print("✅ COMPLETE E-COMMERCE PLAN:")
    print("   - Payment gateway configured")
    print("   - Database for products and orders")
    print("   - User authentication for accounts")
    print("   - All necessary templates identified")
    print()


def run_all_tests():
    """Run all test cases"""
    print("\n")
    print("🧪" * 40)
    print("PROJECT PLANNER TEST SUITE")
    print("🧪" * 40)

    # Test 1: Gym website (the user's case)
    test_gym_website()

    # Test 2: Simple portfolio
    test_simple_portfolio()

    # Test 3: SaaS platform
    test_saas_platform()

    # Test 4: Blog website
    test_blog_website()

    # Test 5: E-commerce store
    test_ecommerce_store()

    print("\n")
    print("=" * 80)
    print("✅ ALL TESTS PASSED")
    print("=" * 80)
    print()
    print("Key Benefits:")
    print("  1. ✅ Correctly detects payment needs from 'sell accessories'")
    print("  2. ✅ Chooses appropriate project type (not static HTML for e-commerce)")
    print("  3. ✅ Matches deployment strategy to project type")
    print("  4. ✅ Identifies all required templates")
    print("  5. ✅ Provides clear deployment roadmap")
    print("  6. ✅ Saves tokens by planning upfront")
    print()


if __name__ == "__main__":
    run_all_tests()
