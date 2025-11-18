#!/usr/bin/env python3
"""
Test Script for Advanced Prompt System
Tests the new structured prompt system with 2,200+ templates

Usage:
    python test_prompt_system.py
    python test_prompt_system.py --verbose
    python test_prompt_system.py --mode structured
    python test_prompt_system.py --mode legacy
"""

import sys
import os
import argparse
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_imports():
    """Test that all modules can be imported"""
    print("\n" + "="*70)
    print("TEST 1: Module Imports")
    print("="*70)

    try:
        from ai_prompts import format_master_prompt, format_component_prompt
        print("✅ ai_prompts.py imported successfully")

        from ai_response_parser import AIResponseParser, parse_project_from_ai
        print("✅ ai_response_parser.py imported successfully")

        from structured_generator import StructuredProjectGenerator
        print("✅ structured_generator.py imported successfully")

        from generation_api import generate_project, update_project
        print("✅ generation_api.py imported successfully")

        from prompt_system_config import (
            should_use_structured,
            print_system_info,
            PromptSystemMode
        )
        print("✅ prompt_system_config.py imported successfully")

        print("\n✅ All modules imported successfully!")
        return True

    except ImportError as e:
        print(f"\n❌ Import failed: {e}")
        return False


def test_prompt_formatting():
    """Test prompt formatting functions"""
    print("\n" + "="*70)
    print("TEST 2: Prompt Formatting")
    print("="*70)

    try:
        from ai_prompts import (
            format_master_prompt,
            format_component_prompt,
            format_update_prompt,
            format_customization_prompt
        )

        # Test master prompt
        master = format_master_prompt("Create a simple website")
        assert len(master) > 100, "Master prompt too short"
        assert "{user_prompt}" not in master, "Placeholder not replaced"
        print("✅ Master prompt formatted correctly")

        # Test component prompt
        component = format_component_prompt(
            component_name="TestComponent",
            user_prompt="Test",
            website_type="saas",
            component_purpose="Testing"
        )
        assert "TestComponent" in component, "Component name missing"
        print("✅ Component prompt formatted correctly")

        # Test update prompt
        update = format_update_prompt(
            modification_request="Add feature",
            project_type="react",
            session_id="test123",
            file_count=5,
            project_memory="Test memory"
        )
        assert "test123" in update, "Session ID missing"
        print("✅ Update prompt formatted correctly")

        print("\n✅ All prompts formatted successfully!")
        return True

    except Exception as e:
        print(f"\n❌ Prompt formatting failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_response_parsing():
    """Test AI response parsing"""
    print("\n" + "="*70)
    print("TEST 3: Response Parsing")
    print("="*70)

    try:
        from ai_response_parser import AIResponseParser

        # Test JSON extraction from markdown
        markdown_json = '''```json
{
  "test": "value",
  "number": 123
}
```'''

        result = AIResponseParser.extract_json(markdown_json)
        assert result is not None, "Failed to extract JSON"
        assert result["test"] == "value", "Incorrect value extracted"
        print("✅ JSON extraction from markdown works")

        # Test direct JSON parsing
        direct_json = '{"test": "value", "number": 123}'
        result = AIResponseParser.extract_json(direct_json)
        assert result is not None, "Failed to parse direct JSON"
        print("✅ Direct JSON parsing works")

        # Test component validation
        good_component = '''
import React from 'react'

export default function TestComponent({ children }) {
  return (
    <div className="test">
      {children}
    </div>
  )
}
'''
        is_valid, error = AIResponseParser.validate_component_completeness(
            good_component,
            "TestComponent"
        )
        assert is_valid, f"Valid component marked as invalid: {error}"
        print("✅ Component validation works")

        # Test incomplete component detection
        bad_component = '''
import React from 'react'

export default function TestComponent({ children }) {
  return (
    <div className="test"
      {children}
'''
        is_valid, error = AIResponseParser.validate_component_completeness(
            bad_component,
            "TestComponent"
        )
        assert not is_valid, "Invalid component marked as valid"
        print("✅ Incomplete component detection works")

        print("\n✅ All parsing tests passed!")
        return True

    except Exception as e:
        print(f"\n❌ Response parsing failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_configuration():
    """Test configuration system"""
    print("\n" + "="*70)
    print("TEST 4: Configuration System")
    print("="*70)

    try:
        from prompt_system_config import (
            should_use_structured,
            should_fallback_on_error,
            get_token_budget,
            set_mode,
            PromptSystemMode,
            print_system_info
        )

        # Test token budgets
        budget = get_token_budget("component_generation")
        assert budget == 3000, f"Wrong token budget: {budget}"
        print("✅ Token budgets configured correctly")

        # Test mode setting
        set_mode(PromptSystemMode.STRUCTURED)
        assert should_use_structured(), "Mode not set to structured"
        print("✅ Mode setting works")

        set_mode(PromptSystemMode.LEGACY)
        assert not should_use_structured(), "Mode not set to legacy"
        print("✅ Mode switching works")

        # Reset to structured for other tests
        set_mode(PromptSystemMode.STRUCTURED)

        # Test system info
        print("\n📋 System Configuration:")
        print_system_info()

        print("\n✅ Configuration system works!")
        return True

    except Exception as e:
        print(f"\n❌ Configuration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_mock_generation():
    """Test generation flow with mocked AI"""
    print("\n" + "="*70)
    print("TEST 5: Mock Generation Flow")
    print("="*70)

    try:
        from structured_generator import StructuredProjectGenerator

        generator = StructuredProjectGenerator()

        # Test config file generation
        config_files = generator._create_config_files("react", {})
        assert "package.json" in config_files, "Missing package.json"
        assert "vite.config.js" in config_files, "Missing vite.config.js"
        assert "index.html" in config_files, "Missing index.html"
        print("✅ Config file generation works")

        # Test fallback component creation
        fallback = generator._create_fallback_component("TestComponent")
        assert "TestComponent" in fallback, "Component name missing"
        assert "export default" in fallback, "Missing export"
        print("✅ Fallback component creation works")

        print("\n✅ Mock generation tests passed!")
        return True

    except Exception as e:
        print(f"\n❌ Mock generation failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_full_integration():
    """Test full integration (requires API key)"""
    print("\n" + "="*70)
    print("TEST 6: Full Integration (Optional)")
    print("="*70)

    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        print("⚠️  SKIPPED: No ANTHROPIC_API_KEY found")
        print("   Set ANTHROPIC_API_KEY to run full integration test")
        return True

    try:
        from generation_api import quick_generate

        print("🚀 Running full generation test (this may take 30-60 seconds)...")
        print("   Prompt: 'Create a simple landing page with header and hero section'")

        files = quick_generate("Create a simple landing page with header and hero section")

        assert files is not None, "No files returned"
        assert len(files) > 0, "Empty files dict returned"

        print(f"\n✅ Generated {len(files)} files:")
        for path in sorted(files.keys())[:10]:  # Show first 10
            file_size = len(files[path])
            print(f"   - {path} ({file_size} bytes)")

        if len(files) > 10:
            print(f"   ... and {len(files) - 10} more files")

        print("\n✅ Full integration test passed!")
        return True

    except Exception as e:
        print(f"\n❌ Full integration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests"""
    parser = argparse.ArgumentParser(description="Test the advanced prompt system")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--mode", choices=["structured", "legacy", "hybrid"],
                       help="Force specific mode")
    parser.add_argument("--skip-integration", action="store_true",
                       help="Skip integration test (faster)")

    args = parser.parse_args()

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        os.environ["VERBOSE_PROMPT_LOGGING"] = "true"

    # Set mode if specified
    if args.mode:
        from prompt_system_config import set_mode, PromptSystemMode
        mode_map = {
            "structured": PromptSystemMode.STRUCTURED,
            "legacy": PromptSystemMode.LEGACY,
            "hybrid": PromptSystemMode.HYBRID
        }
        set_mode(mode_map[args.mode])

    print("\n" + "="*70)
    print("🧪 ADVANCED PROMPT SYSTEM - TEST SUITE")
    print("="*70)

    # Run tests
    results = []

    results.append(("Module Imports", test_imports()))
    results.append(("Prompt Formatting", test_prompt_formatting()))
    results.append(("Response Parsing", test_response_parsing()))
    results.append(("Configuration", test_configuration()))
    results.append(("Mock Generation", test_mock_generation()))

    if not args.skip_integration:
        results.append(("Full Integration", test_full_integration()))

    # Summary
    print("\n" + "="*70)
    print("📊 TEST SUMMARY")
    print("="*70)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")

    print("\n" + "="*70)

    if passed == total:
        print(f"🎉 ALL TESTS PASSED ({passed}/{total})")
        print("="*70)
        print("\n✅ The advanced prompt system is ready to use!")
        print("\nNext steps:")
        print("1. Read QUICKSTART.md for usage examples")
        print("2. Read PROMPT_SYSTEM_README.md for detailed documentation")
        print("3. Try: python -c \"from generation_api import quick_generate; print('System ready!')\"")
        return 0
    else:
        print(f"❌ SOME TESTS FAILED ({passed}/{total} passed)")
        print("="*70)
        print("\n⚠️  Please fix the failing tests before using the system.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
