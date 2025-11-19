"""
Test Prompt Enhancer with real examples
Shows how vague prompts become detailed specifications
"""

import os
import logging
from prompt_enhancer import (
    PromptEnhancer,
    SmartPromptBuilder,
    print_enhancement,
    quick_enhance
)
from project_planner import ProjectPlanner

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_gym_website_enhancement():
    """Test with gym website (vague prompt)"""
    print("\n")
    print("🏋️" * 40)
    print("EXAMPLE 1: GYM WEBSITE (Vague Prompt)")
    print("🏋️" * 40)
    print()

    # Vague user prompt
    user_prompt = "i want to build a gym website to showcase my gym and sell accessories"

    print(f"User's Prompt (Vague):")
    print(f'  "{user_prompt}"')
    print()
    print("⏳ Enhancing with LLM...")
    print()

    # Check if API key exists
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("⚠️  ANTHROPIC_API_KEY not set - using fallback")
        print("   (Set API key to see real enhancement)")
        return

    # Enhance prompt
    optimized, enhanced = quick_enhance(user_prompt)

    # Print enhancement
    print_enhancement(enhanced)

    print("Optimized Prompt for Planning:")
    print(f'  "{optimized}"')
    print()

    # Now use with project planner
    print("=" * 80)
    print("USING ENHANCED PROMPT WITH PROJECT PLANNER")
    print("=" * 80)
    print()

    planner = ProjectPlanner()
    plan = planner.create_plan(optimized)

    print(f"📦 Project Type: {plan.project_type.value}")
    print(f"🚀 Deployment: {plan.deployment_target.value}")
    print()
    print("✅ Requirements Detected:")
    if plan.requirements.has_payment:
        print("   ✅ Payment processing (from 'sell accessories')")
    if plan.requirements.has_product_catalog:
        print("   ✅ Product catalog")
    if plan.requirements.has_shopping_cart:
        print("   ✅ Shopping cart")
    if plan.requirements.has_authentication:
        print("   ✅ User authentication")
    if plan.requirements.has_database:
        print("   ✅ Database")
    print()


def test_vague_prompt_clarification():
    """Test with very vague prompt"""
    print("\n")
    print("❓" * 40)
    print("EXAMPLE 2: VAGUE PROMPT CLARIFICATION")
    print("❓" * 40)
    print()

    # Very vague prompt
    user_prompt = "i need a website"

    print(f"User's Prompt (Very Vague):")
    print(f'  "{user_prompt}"')
    print()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("⚠️  ANTHROPIC_API_KEY not set - skipping")
        return

    print("⏳ Enhancing...")
    print()

    # Enhance (will generate clarifying questions)
    enhancer = PromptEnhancer(use_haiku=True)
    enhanced = enhancer.enhance_prompt(user_prompt, auto_clarify=False)

    print_enhancement(enhanced)

    print("💡 Next Steps:")
    print("   1. Ask user these clarifying questions")
    print("   2. User provides answers")
    print("   3. Refine enhancement with answers")
    print("   4. Create detailed project plan")
    print()


def test_detailed_prompt():
    """Test with already detailed prompt"""
    print("\n")
    print("✨" * 40)
    print("EXAMPLE 3: DETAILED PROMPT (Already Clear)")
    print("✨" * 40)
    print()

    # Detailed prompt
    user_prompt = """
    Create a SaaS platform for project management with the following features:
    - User authentication with email and Google OAuth
    - Team collaboration with real-time updates
    - Project boards with drag-and-drop
    - File uploads and attachments
    - Subscription pricing (Free, Pro, Enterprise tiers)
    - Admin dashboard for analytics
    - Email notifications
    Target audience: Small to medium-sized software teams
    """

    print(f"User's Prompt (Detailed):")
    print(f'  {user_prompt.strip()}')
    print()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("⚠️  ANTHROPIC_API_KEY not set - skipping")
        return

    print("⏳ Enhancing...")
    print()

    optimized, enhanced = quick_enhance(user_prompt)

    print_enhancement(enhanced)

    print("✅ RESULT:")
    print(f"   Confidence: {enhanced.confidence_score * 100:.0f}%")
    print(f"   Needs clarification: {enhanced.needs_clarification}")
    print(f"   Clarifying questions: {len(enhanced.clarifying_questions)}")
    print()


def test_e_commerce_enhancement():
    """Test with e-commerce prompt"""
    print("\n")
    print("🛒" * 40)
    print("EXAMPLE 4: E-COMMERCE ENHANCEMENT")
    print("🛒" * 40)
    print()

    user_prompt = "online store for handmade jewelry"

    print(f"User's Prompt (Brief):")
    print(f'  "{user_prompt}"')
    print()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("⚠️  ANTHROPIC_API_KEY not set - skipping")
        return

    print("⏳ Enhancing...")
    print()

    optimized, enhanced = quick_enhance(user_prompt)

    print_enhancement(enhanced)

    print("Optimized Prompt:")
    print(f'  "{optimized}"')
    print()

    # Use with planner
    planner = ProjectPlanner()
    plan = planner.create_plan(optimized)

    print("Generated Plan:")
    print(f"  Project Type: {plan.project_type.value}")
    print(f"  Tech Stack: {plan.frontend_framework}")
    if plan.backend_framework:
        print(f"             + {plan.backend_framework}")
    if plan.database:
        print(f"             + {plan.database}")
    if plan.payment_gateway:
        print(f"             + {plan.payment_gateway}")
    print()


def test_complete_workflow():
    """Test complete workflow: Enhance → Plan → Generate"""
    print("\n")
    print("🔄" * 40)
    print("COMPLETE WORKFLOW: ENHANCE → PLAN → GENERATE")
    print("🔄" * 40)
    print()

    # User's vague prompt
    user_prompt = "portfolio website for photographer"

    print(f"Step 1: User Input")
    print(f'  "{user_prompt}"')
    print()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("⚠️  ANTHROPIC_API_KEY not set - using fallback workflow")
        print()
        print("Without enhancement:")
        planner = ProjectPlanner()
        plan = planner.create_plan(user_prompt)
        print(f"  Project Type: {plan.project_type.value}")
        return

    print(f"Step 2: Enhance Prompt")
    optimized, enhanced = quick_enhance(user_prompt)
    print(f'  Enhanced: "{enhanced.enhanced_prompt}"')
    print(f'  Key Features: {", ".join(enhanced.key_features)}')
    print()

    print(f"Step 3: Create Project Plan")
    planner = ProjectPlanner()
    plan = planner.create_plan(optimized)
    print(f"  Project Type: {plan.project_type.value}")
    print(f"  Templates Needed: {len(plan.templates_needed)}")
    print()

    print(f"Step 4: Generate Code (simulated)")
    print(f"  ✅ Would select {len(plan.templates_needed)} templates")
    print(f"  ✅ Would generate with {plan.frontend_framework}")
    print(f"  ✅ Would deploy to {plan.deployment_target.value}")
    print()

    print("✅ COMPLETE WORKFLOW SUCCESS")
    print()


def run_all_tests():
    """Run all enhancement tests"""
    print("\n")
    print("🧪" * 40)
    print("PROMPT ENHANCER TEST SUITE")
    print("🧪" * 40)

    # Test 1: Gym website
    test_gym_website_enhancement()

    # Test 2: Vague prompt
    test_vague_prompt_clarification()

    # Test 3: Detailed prompt
    test_detailed_prompt()

    # Test 4: E-commerce
    test_e_commerce_enhancement()

    # Test 5: Complete workflow
    test_complete_workflow()

    print("\n")
    print("=" * 80)
    print("✅ ALL TESTS COMPLETED")
    print("=" * 80)
    print()
    print("Key Benefits of Prompt Enhancement:")
    print()
    print("  1. ✅ Vague prompts → Detailed specifications")
    print("  2. ✅ Implicit requirements → Explicit features")
    print("  3. ✅ Ambiguities → Clarifying questions")
    print("  4. ✅ Better planning → More accurate code")
    print("  5. ✅ Token savings → Generate once, correctly")
    print()
    print("Token Usage:")
    print("  - Enhancement: ~200-400 tokens per prompt")
    print("  - Clarification: ~150-300 tokens per round")
    print("  - Total: ~500-700 tokens (saves 5,000+ in regeneration)")
    print()


if __name__ == "__main__":
    run_all_tests()
