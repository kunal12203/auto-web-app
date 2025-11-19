"""
Unified Generation API
Provides a simple interface that works with both legacy and structured prompt systems
Handles feature flags, fallbacks, and error recovery automatically
"""

import logging
from typing import Dict, Optional, Any

from prompt_system_config import (
    should_use_structured,
    should_fallback_on_error,
    log_prompt_info,
    get_token_budget
)

logger = logging.getLogger(__name__)

# ============================================================================
# MAIN GENERATION API
# ============================================================================

def generate_project(
    user_prompt: str,
    project_name: str = "my-project",
    project_type: Optional[str] = None,
    payment_gateway: Optional[str] = None
) -> Dict[str, str]:
    """
    Generate a complete project from user prompt

    This function automatically chooses between structured and legacy systems
    based on configuration. Falls back gracefully on errors.

    Args:
        user_prompt: User's description of what to build
        project_name: Name for the project
        project_type: "react" | "fullstack" | "simple" (auto-detected if None)
        payment_gateway: "stripe" | "paypal" | "razorpay" | None

    Returns:
        Dict mapping file paths to file contents
        {
            "src/App.jsx": "...",
            "src/components/Header.jsx": "...",
            "package.json": "...",
            ...
        }
    """
    log_prompt_info(f"Generating project: {project_name}")
    log_prompt_info(f"Prompt: {user_prompt[:100]}...")

    # Try structured system if enabled
    if should_use_structured():
        try:
            log_prompt_info("Using STRUCTURED prompt system")

            from structured_generator import generate_project_structured

            files = generate_project_structured(user_prompt)

            if files:
                # Add payment integration if requested
                if payment_gateway:
                    files.update(_add_payment_integration(payment_gateway, files))

                log_prompt_info(f"✅ Structured generation successful: {len(files)} files")
                return files
            else:
                log_prompt_info("⚠️ Structured generation returned no files", "warning")

                if should_fallback_on_error():
                    log_prompt_info("Falling back to LEGACY system...")
                else:
                    return {}

        except Exception as e:
            log_prompt_info(f"❌ Structured generation failed: {e}", "error")

            if should_fallback_on_error():
                log_prompt_info("Falling back to LEGACY system...")
            else:
                raise

    # Use legacy system (either by choice or fallback)
    log_prompt_info("Using LEGACY prompt system")

    try:
        # Import the existing generation function from main.py
        # This would need to be refactored out of main.py first
        # For now, we'll provide the structure

        from main import generate_project_files

        files = generate_project_files(
            prompt=user_prompt,
            project_name=project_name,
            project_type=project_type or "react",
            payment_gateway=payment_gateway
        )

        log_prompt_info(f"✅ Legacy generation successful: {len(files)} files")
        return files

    except ImportError:
        log_prompt_info("⚠️ Legacy system not available (generate_project_files not found)", "warning")
        log_prompt_info("Please ensure main.py exports generate_project_files function", "warning")
        return {}

    except Exception as e:
        log_prompt_info(f"❌ Legacy generation failed: {e}", "error")
        raise


def update_project(
    modification_request: str,
    session_id: str,
    current_files: Dict[str, str],
    project_memory: str,
    project_type: str = "react"
) -> Dict:
    """
    Update an existing project with multi-turn modifications

    Args:
        modification_request: What the user wants to change/add
        session_id: Unique session identifier
        current_files: Current project files
        project_memory: Compressed project context
        project_type: Type of project

    Returns:
        Update plan or updated files depending on mode
        {
            "modificationType": "update|add|delete|refactor",
            "filesToModify": [...],
            "filesToAdd": [...],
            "filesToDelete": [...],
            "updatedFiles": {...}  # Actual file contents
        }
    """
    log_prompt_info(f"Processing update for session: {session_id}")
    log_prompt_info(f"Request: {modification_request[:100]}...")

    # Try structured system if enabled
    if should_use_structured():
        try:
            log_prompt_info("Using STRUCTURED update system")

            from structured_generator import update_project_structured

            update_plan = update_project_structured(
                modification_request=modification_request,
                project_type=project_type,
                session_id=session_id,
                current_files=current_files,
                project_memory=project_memory
            )

            if update_plan:
                # Apply the update plan to generate actual updated files
                updated_files = _apply_update_plan(update_plan, current_files, project_memory)

                result = {
                    **update_plan,
                    "updatedFiles": updated_files
                }

                log_prompt_info(f"✅ Structured update successful")
                return result
            else:
                log_prompt_info("⚠️ Structured update returned no plan", "warning")

                if should_fallback_on_error():
                    log_prompt_info("Falling back to LEGACY update...")
                else:
                    return {}

        except Exception as e:
            log_prompt_info(f"❌ Structured update failed: {e}", "error")

            if should_fallback_on_error():
                log_prompt_info("Falling back to LEGACY update...")
            else:
                raise

    # Use legacy update system
    log_prompt_info("Using LEGACY update system")

    try:
        # This would use the existing multi-turn logic from main.py
        # For now, return a simplified structure

        return {
            "modificationType": "update",
            "filesToModify": [],
            "filesToAdd": [],
            "filesToDelete": [],
            "updatedFiles": current_files  # Placeholder
        }

    except Exception as e:
        log_prompt_info(f"❌ Legacy update failed: {e}", "error")
        raise


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def _add_payment_integration(gateway: str, current_files: Dict[str, str]) -> Dict[str, str]:
    """
    Add payment integration files to project

    Args:
        gateway: "stripe" | "paypal" | "razorpay"
        current_files: Existing project files

    Returns:
        Additional files for payment integration
    """
    log_prompt_info(f"Adding {gateway} payment integration")

    try:
        from payment_templates import get_payment_files

        payment_files = get_payment_files(gateway)
        log_prompt_info(f"✅ Added {len(payment_files)} payment files")

        return payment_files

    except Exception as e:
        log_prompt_info(f"⚠️ Failed to add payment integration: {e}", "warning")
        return {}


def _apply_update_plan(
    update_plan: Dict,
    current_files: Dict[str, str],
    project_memory: str
) -> Dict[str, str]:
    """
    Apply an update plan to generate updated file contents

    Args:
        update_plan: Structured update plan from AI
        current_files: Current project files
        project_memory: Project context

    Returns:
        Updated files
    """
    log_prompt_info("Applying update plan...")

    updated_files = current_files.copy()

    # Handle file modifications
    for modification in update_plan.get("filesToModify", []):
        file_path = modification["path"]
        changes = modification["changes"]
        template = modification.get("template")

        log_prompt_info(f"   Modifying: {file_path}")

        if template and template != "use existing":
            # Load from template
            try:
                from component_templates import load_matched_components

                component_name = file_path.split("/")[-1].replace(".jsx", "")
                loaded = load_matched_components({component_name: template}, {})

                if component_name in loaded:
                    updated_files[file_path] = loaded[component_name]
                    log_prompt_info(f"      ✅ Loaded from template: {template}")

            except Exception as e:
                log_prompt_info(f"      ⚠️ Template load failed: {e}", "warning")
                # Fall back to AI modification
                _modify_file_with_ai(file_path, changes, updated_files)
        else:
            # Modify with AI
            _modify_file_with_ai(file_path, changes, updated_files)

    # Handle new files
    for addition in update_plan.get("filesToAdd", []):
        file_path = addition["path"]
        template = addition.get("template")
        reason = addition.get("reason", "")

        log_prompt_info(f"   Adding: {file_path}")

        if template:
            # Generate from template
            try:
                from component_templates import load_matched_components

                component_name = file_path.split("/")[-1].replace(".jsx", "").replace(".js", "")
                loaded = load_matched_components({component_name: template}, {})

                if component_name in loaded:
                    updated_files[file_path] = loaded[component_name]
                    log_prompt_info(f"      ✅ Created from template: {template}")

            except Exception as e:
                log_prompt_info(f"      ⚠️ Template creation failed: {e}", "warning")
                # Fall back to AI generation
                _generate_file_with_ai(file_path, reason, updated_files)
        else:
            # Generate with AI
            _generate_file_with_ai(file_path, reason, updated_files)

    # Handle deletions
    for file_path in update_plan.get("filesToDelete", []):
        if file_path in updated_files:
            del updated_files[file_path]
            log_prompt_info(f"   Deleted: {file_path}")

    log_prompt_info(f"✅ Update plan applied: {len(updated_files)} files")

    return updated_files


def _modify_file_with_ai(file_path: str, changes: str, files: Dict[str, str]):
    """Modify a file using AI (placeholder for actual implementation)"""
    log_prompt_info(f"      Modifying with AI: {changes[:50]}...")

    # This would call the AI to modify the file
    # For now, keep the file as-is
    pass


def _generate_file_with_ai(file_path: str, purpose: str, files: Dict[str, str]):
    """Generate a new file using AI (placeholder for actual implementation)"""
    log_prompt_info(f"      Generating with AI: {purpose[:50]}...")

    # This would call the AI to generate the file
    # For now, create a placeholder
    files[file_path] = f"// Generated file: {file_path}\n// Purpose: {purpose}\n"


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

def quick_generate(prompt: str) -> Dict[str, str]:
    """Quick generation with default settings"""
    return generate_project(
        user_prompt=prompt,
        project_name="quick-project",
        project_type=None,
        payment_gateway=None
    )


def quick_update(request: str, session_id: str, files: Dict[str, str], memory: str) -> Dict:
    """Quick update with default settings"""
    return update_project(
        modification_request=request,
        session_id=session_id,
        current_files=files,
        project_memory=memory,
        project_type="react"
    )


# ============================================================================
# USAGE EXAMPLES
# ============================================================================

"""
Example 1: Basic Project Generation
-----------------------------------
from generation_api import generate_project

files = generate_project(
    user_prompt="Create a modern SaaS landing page",
    project_name="my-saas",
    project_type="react"
)

# Files will be generated using best available system
# (structured or legacy based on config)


Example 2: With Payment Integration
-----------------------------------
files = generate_project(
    user_prompt="Build an e-commerce store",
    project_name="my-store",
    payment_gateway="stripe"
)


Example 3: Multi-Turn Update
----------------------------
from generation_api import update_project

# Initial generation
files = generate_project("Create a blog")

# User wants to add a feature
update_result = update_project(
    modification_request="Add a search bar",
    session_id="abc123",
    current_files=files,
    project_memory=memory_string
)

# Access updated files
updated_files = update_result["updatedFiles"]


Example 4: Quick Generation
---------------------------
from generation_api import quick_generate

files = quick_generate("Portfolio site for a photographer")


Example 5: Force Mode at Runtime
--------------------------------
from prompt_system_config import set_mode, PromptSystemMode

# Force use of structured system
set_mode(PromptSystemMode.STRUCTURED)
files = quick_generate("Landing page")

# Force use of legacy system
set_mode(PromptSystemMode.LEGACY)
files = quick_generate("Landing page")

# Use hybrid (try structured, fallback to legacy)
set_mode(PromptSystemMode.HYBRID)
files = quick_generate("Landing page")
"""
