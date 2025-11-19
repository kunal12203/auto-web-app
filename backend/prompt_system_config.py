"""
Prompt System Configuration
Feature flags and settings for the advanced prompt system
"""

import os
import logging

logger = logging.getLogger(__name__)

# ============================================================================
# FEATURE FLAGS
# ============================================================================

# Enable the new structured prompt system
# Set to True to use JSON-based prompts with structured outputs
# Set to False to use the original prompt system
USE_STRUCTURED_PROMPTS = os.getenv("USE_STRUCTURED_PROMPTS", "true").lower() == "true"

# Enable verbose logging for prompt system debugging
VERBOSE_PROMPT_LOGGING = os.getenv("VERBOSE_PROMPT_LOGGING", "false").lower() == "true"

# Enable automatic fallback to old system if structured fails
AUTO_FALLBACK_ON_ERROR = os.getenv("AUTO_FALLBACK_ON_ERROR", "true").lower() == "true"

# Maximum retries for structured generation
MAX_STRUCTURED_RETRIES = int(os.getenv("MAX_STRUCTURED_RETRIES", "2"))

# Token budgets for different generation types
TOKEN_BUDGETS = {
    "project_structure": 4096,  # Getting the initial file structure plan
    "component_generation": 3000,  # First attempt at generating a component
    "component_generation_retry": 4500,  # Retry with more tokens
    "multi_turn_update": 3000,  # Processing update requests
    "template_customization": 500,  # Filling template placeholders
    "error_fix": 2000,  # Fixing errors in generated code
}

# ============================================================================
# SYSTEM MODES
# ============================================================================

class PromptSystemMode:
    """Enum-like class for prompt system modes"""
    LEGACY = "legacy"  # Original unstructured prompts
    STRUCTURED = "structured"  # New JSON-based prompts
    HYBRID = "hybrid"  # Try structured, fallback to legacy
    AUTO = "auto"  # Intelligently choose based on request

# Current mode (can be overridden at runtime)
CURRENT_MODE = (
    PromptSystemMode.STRUCTURED if USE_STRUCTURED_PROMPTS
    else PromptSystemMode.LEGACY
)

# ============================================================================
# CONFIGURATION HELPERS
# ============================================================================

def get_token_budget(generation_type: str) -> int:
    """Get token budget for a specific generation type"""
    return TOKEN_BUDGETS.get(generation_type, 3000)


def should_use_structured() -> bool:
    """Check if structured prompt system should be used"""
    return CURRENT_MODE in [PromptSystemMode.STRUCTURED, PromptSystemMode.HYBRID, PromptSystemMode.AUTO]


def should_fallback_on_error() -> bool:
    """Check if system should fallback to legacy on errors"""
    return AUTO_FALLBACK_ON_ERROR or CURRENT_MODE == PromptSystemMode.HYBRID


def log_prompt_info(message: str, level: str = "info"):
    """Log prompt system messages if verbose logging is enabled"""
    if VERBOSE_PROMPT_LOGGING or level == "error":
        getattr(logger, level)(f"[Prompt System] {message}")


def set_mode(mode: str):
    """
    Dynamically set the prompt system mode

    Args:
        mode: One of "legacy", "structured", "hybrid", "auto"
    """
    global CURRENT_MODE

    if mode in [PromptSystemMode.LEGACY, PromptSystemMode.STRUCTURED,
                PromptSystemMode.HYBRID, PromptSystemMode.AUTO]:
        CURRENT_MODE = mode
        logger.info(f"✅ Prompt system mode set to: {mode}")
    else:
        logger.warning(f"⚠️ Invalid mode: {mode}. Using current mode: {CURRENT_MODE}")


# ============================================================================
# STARTUP INFO
# ============================================================================

def print_system_info():
    """Print configuration info on startup"""
    logger.info("=" * 60)
    logger.info("🎯 PROMPT SYSTEM CONFIGURATION")
    logger.info("=" * 60)
    logger.info(f"Mode: {CURRENT_MODE}")
    logger.info(f"Structured Prompts: {'✅ Enabled' if USE_STRUCTURED_PROMPTS else '❌ Disabled'}")
    logger.info(f"Auto Fallback: {'✅ Enabled' if AUTO_FALLBACK_ON_ERROR else '❌ Disabled'}")
    logger.info(f"Verbose Logging: {'✅ Enabled' if VERBOSE_PROMPT_LOGGING else '❌ Disabled'}")
    logger.info(f"Max Retries: {MAX_STRUCTURED_RETRIES}")
    logger.info("=" * 60)


# ============================================================================
# ENVIRONMENT VARIABLE REFERENCE
# ============================================================================

"""
Set these environment variables to configure the prompt system:

USE_STRUCTURED_PROMPTS=true|false
  - Enable/disable the new structured JSON-based prompt system
  - Default: true

AUTO_FALLBACK_ON_ERROR=true|false
  - Automatically fallback to legacy system if structured fails
  - Default: true

VERBOSE_PROMPT_LOGGING=true|false
  - Enable detailed logging for debugging
  - Default: false

MAX_STRUCTURED_RETRIES=<number>
  - Maximum retry attempts for structured generation
  - Default: 2

Example .env file:
```
USE_STRUCTURED_PROMPTS=true
AUTO_FALLBACK_ON_ERROR=true
VERBOSE_PROMPT_LOGGING=false
MAX_STRUCTURED_RETRIES=2
```

To switch modes at runtime:
```python
from prompt_system_config import set_mode, PromptSystemMode

set_mode(PromptSystemMode.STRUCTURED)  # Use structured
set_mode(PromptSystemMode.LEGACY)  # Use legacy
set_mode(PromptSystemMode.HYBRID)  # Try structured, fallback to legacy
```
"""
