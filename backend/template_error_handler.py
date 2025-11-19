"""
Template Error Handler - Detects and fixes common template generation errors
Uses rule-based fixes (zero tokens) with LLM fallback (minimal tokens)
"""

import re
import logging
from typing import Optional, Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


# ============================================================================
# ERROR CLASSIFICATION
# ============================================================================

class ErrorType(Enum):
    """Types of errors that can occur in template generation"""
    SYNTAX_ERROR = "syntax_error"
    JSX_ERROR = "jsx_error"
    IMPORT_ERROR = "import_error"
    BRACE_MISMATCH = "brace_mismatch"
    QUOTE_ERROR = "quote_error"
    COMPONENT_NAME_ERROR = "component_name_error"
    UNCLOSED_TAG = "unclosed_tag"
    MISSING_EXPORT = "missing_export"
    DUPLICATE_IMPORT = "duplicate_import"
    UNKNOWN = "unknown"


@dataclass
class ErrorInfo:
    """Information about a detected error"""
    error_type: ErrorType
    line_number: Optional[int]
    column: Optional[int]
    message: str
    code_snippet: Optional[str]
    fix_confidence: float  # 0.0 to 1.0


@dataclass
class FixResult:
    """Result of attempting to fix an error"""
    success: bool
    fixed_code: Optional[str]
    fix_method: str  # "rule_based", "llm", "manual_required"
    error_type: ErrorType
    message: str
    tokens_used: int = 0


# ============================================================================
# ERROR DETECTOR
# ============================================================================

class TemplateErrorDetector:
    """
    Detects errors in generated template code
    Fast, zero-token detection using regex and AST parsing
    """

    def __init__(self):
        self.common_patterns = self._load_common_patterns()

    def _load_common_patterns(self) -> Dict[ErrorType, List[str]]:
        """Load common error patterns"""
        return {
            ErrorType.JSX_ERROR: [
                r'f-string.*cannot include.*backslash',
                r'Single.*}.*encountered in format string',
                r'invalid syntax.*className.*{',
            ],
            ErrorType.BRACE_MISMATCH: [
                r'unmatched.*}',
                r'unmatched.*{',
                r'SyntaxError:.*brace',
            ],
            ErrorType.IMPORT_ERROR: [
                r'ImportError',
                r'ModuleNotFoundError',
                r'cannot import',
            ],
            ErrorType.MISSING_EXPORT: [
                r'export default.*not found',
            ],
        }

    def detect_errors(self, code: str, component_name: str) -> List[ErrorInfo]:
        """
        Detect all errors in code

        Returns:
            List of detected errors with confidence scores
        """
        errors = []

        # Check for missing React import
        if 'import React' not in code and 'from React' not in code:
            errors.append(ErrorInfo(
                error_type=ErrorType.IMPORT_ERROR,
                line_number=1,
                column=0,
                message="Missing React import",
                code_snippet=None,
                fix_confidence=1.0
            ))

        # Check for missing export
        if f'export default {component_name}' not in code:
            errors.append(ErrorInfo(
                error_type=ErrorType.MISSING_EXPORT,
                line_number=None,
                column=None,
                message=f"Missing export default {component_name}",
                code_snippet=None,
                fix_confidence=1.0
            ))

        # Check for brace balance
        brace_error = self._check_brace_balance(code)
        if brace_error:
            errors.append(brace_error)

        # Check for unclosed JSX tags
        jsx_errors = self._check_jsx_tags(code)
        errors.extend(jsx_errors)

        # Check for quote issues
        quote_errors = self._check_quotes(code)
        errors.extend(quote_errors)

        # Check for duplicate imports
        duplicate_imports = self._check_duplicate_imports(code)
        if duplicate_imports:
            errors.append(duplicate_imports)

        return errors

    def _check_brace_balance(self, code: str) -> Optional[ErrorInfo]:
        """Check if braces are balanced"""
        # Count braces outside of strings
        open_count = 0
        close_count = 0
        in_string = False
        escape_next = False

        for i, char in enumerate(code):
            if escape_next:
                escape_next = False
                continue

            if char == '\\':
                escape_next = True
                continue

            if char in ['"', "'", '`']:
                in_string = not in_string

            if not in_string:
                if char == '{':
                    open_count += 1
                elif char == '}':
                    close_count += 1

        if open_count != close_count:
            return ErrorInfo(
                error_type=ErrorType.BRACE_MISMATCH,
                line_number=None,
                column=None,
                message=f"Brace mismatch: {open_count} open, {close_count} close",
                code_snippet=None,
                fix_confidence=0.8
            )

        return None

    def _check_jsx_tags(self, code: str) -> List[ErrorInfo]:
        """Check for unclosed JSX tags"""
        errors = []

        # Simple tag matching (not perfect but catches common issues)
        # Match opening tags like <div>, <Button>
        opening_tags = re.findall(r'<(\w+)(?:\s|>|/>)', code)
        # Match closing tags like </div>
        closing_tags = re.findall(r'</(\w+)>', code)
        # Match self-closing tags like <input />
        self_closing = re.findall(r'<(\w+)\s+[^>]*?/>', code)

        # Remove self-closing from opening tags
        for tag in self_closing:
            if tag in opening_tags:
                opening_tags.remove(tag)

        # Check balance
        for tag in set(opening_tags):
            open_count = opening_tags.count(tag)
            close_count = closing_tags.count(tag)

            if open_count != close_count:
                errors.append(ErrorInfo(
                    error_type=ErrorType.UNCLOSED_TAG,
                    line_number=None,
                    column=None,
                    message=f"Tag <{tag}> mismatch: {open_count} open, {close_count} close",
                    code_snippet=None,
                    fix_confidence=0.7
                ))

        return errors

    def _check_quotes(self, code: str) -> List[ErrorInfo]:
        """Check for quote issues"""
        errors = []

        # Check for unescaped quotes in f-strings
        fstring_pattern = r'f[\'"].*?[\'"]'
        fstrings = re.findall(fstring_pattern, code, re.DOTALL)

        for fstring in fstrings:
            # Check if there are unescaped quotes inside
            if '\\' in fstring and ('{' in fstring or '}' in fstring):
                errors.append(ErrorInfo(
                    error_type=ErrorType.QUOTE_ERROR,
                    line_number=None,
                    column=None,
                    message="Backslash in f-string expression",
                    code_snippet=fstring[:100],
                    fix_confidence=0.9
                ))

        return errors

    def _check_duplicate_imports(self, code: str) -> Optional[ErrorInfo]:
        """Check for duplicate imports"""
        import_lines = []
        for line in code.split('\n'):
            if line.strip().startswith('import '):
                import_lines.append(line.strip())

        if len(import_lines) != len(set(import_lines)):
            return ErrorInfo(
                error_type=ErrorType.DUPLICATE_IMPORT,
                line_number=None,
                column=None,
                message="Duplicate import statements detected",
                code_snippet=None,
                fix_confidence=1.0
            )

        return None


# ============================================================================
# RULE-BASED ERROR FIXER
# ============================================================================

class RuleBasedFixer:
    """
    Fixes common errors using predefined rules
    Zero tokens - no LLM needed
    """

    def __init__(self):
        self.fix_count = 0

    def fix_error(self, code: str, error: ErrorInfo, component_name: str) -> Optional[FixResult]:
        """
        Attempt to fix error using rules

        Returns:
            FixResult if fixed, None if cannot fix with rules
        """
        if error.error_type == ErrorType.IMPORT_ERROR:
            return self._fix_missing_import(code, error)

        elif error.error_type == ErrorType.MISSING_EXPORT:
            return self._fix_missing_export(code, error, component_name)

        elif error.error_type == ErrorType.DUPLICATE_IMPORT:
            return self._fix_duplicate_imports(code, error)

        elif error.error_type == ErrorType.QUOTE_ERROR:
            return self._fix_quote_error(code, error)

        elif error.error_type == ErrorType.JSX_ERROR:
            return self._fix_jsx_error(code, error)

        elif error.error_type == ErrorType.BRACE_MISMATCH:
            return self._fix_brace_mismatch(code, error)

        return None

    def _fix_missing_import(self, code: str, error: ErrorInfo) -> FixResult:
        """Add missing React import"""
        if 'import React' not in code:
            fixed_code = "import React from 'react'\n" + code
            return FixResult(
                success=True,
                fixed_code=fixed_code,
                fix_method="rule_based",
                error_type=error.error_type,
                message="Added React import",
                tokens_used=0
            )

        return FixResult(
            success=False,
            fixed_code=None,
            fix_method="rule_based",
            error_type=error.error_type,
            message="Could not fix import",
            tokens_used=0
        )

    def _fix_missing_export(self, code: str, error: ErrorInfo, component_name: str) -> FixResult:
        """Add missing export statement"""
        if f'export default {component_name}' not in code:
            # Find the end of the component (after last closing brace)
            lines = code.split('\n')

            # Find last non-empty line
            for i in range(len(lines) - 1, -1, -1):
                if lines[i].strip():
                    # Add export after it
                    lines.insert(i + 1, f'\nexport default {component_name};')
                    break

            fixed_code = '\n'.join(lines)
            return FixResult(
                success=True,
                fixed_code=fixed_code,
                fix_method="rule_based",
                error_type=error.error_type,
                message=f"Added export default {component_name}",
                tokens_used=0
            )

        return FixResult(
            success=False,
            fixed_code=None,
            fix_method="rule_based",
            error_type=error.error_type,
            message="Export already exists",
            tokens_used=0
        )

    def _fix_duplicate_imports(self, code: str, error: ErrorInfo) -> FixResult:
        """Remove duplicate import statements"""
        lines = code.split('\n')
        seen_imports = set()
        fixed_lines = []

        for line in lines:
            if line.strip().startswith('import '):
                if line.strip() not in seen_imports:
                    seen_imports.add(line.strip())
                    fixed_lines.append(line)
                # else: skip duplicate
            else:
                fixed_lines.append(line)

        fixed_code = '\n'.join(fixed_lines)
        return FixResult(
            success=True,
            fixed_code=fixed_code,
            fix_method="rule_based",
            error_type=error.error_type,
            message="Removed duplicate imports",
            tokens_used=0
        )

    def _fix_quote_error(self, code: str, error: ErrorInfo) -> Optional[FixResult]:
        """Fix quote escaping errors"""
        # Common pattern: f-strings with backslashes in expressions
        # Cannot be easily fixed with rules - need LLM or manual fix
        return None

    def _fix_jsx_error(self, code: str, error: ErrorInfo) -> Optional[FixResult]:
        """Fix JSX-related errors"""
        # Common pattern: className={something} in f-string
        # This is complex - better to use LLM
        return None

    def _fix_brace_mismatch(self, code: str, error: ErrorInfo) -> Optional[FixResult]:
        """Attempt to fix brace mismatch"""
        # Count braces
        open_count = code.count('{')
        close_count = code.count('}')

        if open_count > close_count:
            # Add missing closing braces
            diff = open_count - close_count
            fixed_code = code + ('}' * diff)

            return FixResult(
                success=True,
                fixed_code=fixed_code,
                fix_method="rule_based",
                error_type=error.error_type,
                message=f"Added {diff} missing closing braces",
                tokens_used=0
            )
        elif close_count > open_count:
            # Remove extra closing braces from end
            diff = close_count - open_count
            # Remove from end
            for _ in range(diff):
                idx = code.rfind('}')
                if idx != -1:
                    code = code[:idx] + code[idx+1:]

            return FixResult(
                success=True,
                fixed_code=code,
                fix_method="rule_based",
                error_type=error.error_type,
                message=f"Removed {diff} extra closing braces",
                tokens_used=0
            )

        return None


# ============================================================================
# LLM-BASED FIXER (FALLBACK)
# ============================================================================

class LLMFixer:
    """
    Uses LLM to fix complex errors that rules cannot handle
    Minimizes token usage with targeted prompts
    """

    def __init__(self, use_haiku: bool = True):
        """
        Args:
            use_haiku: Use Claude Haiku for cheap fixes (default True)
        """
        self.use_haiku = use_haiku
        self.total_tokens_used = 0

    def fix_error(
        self,
        code: str,
        error: ErrorInfo,
        component_name: str
    ) -> FixResult:
        """
        Fix error using LLM

        Uses minimal prompt to reduce tokens:
        - Only sends error context (not full code if possible)
        - Asks for fix only, not explanation
        - Uses Haiku by default
        """
        try:
            # Import here to avoid circular dependency
            import anthropic
            import os

            client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

            # Build minimal prompt
            prompt = self._build_minimal_prompt(code, error, component_name)

            # Use Haiku for cost efficiency
            model = "claude-haiku-3-5-20241022" if self.use_haiku else "claude-sonnet-4-5-20250929"

            response = client.messages.create(
                model=model,
                max_tokens=500,  # Keep it short
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )

            # Extract fixed code
            fixed_code = self._extract_code(response.content[0].text)

            # Track tokens
            tokens_used = response.usage.input_tokens + response.usage.output_tokens
            self.total_tokens_used += tokens_used

            return FixResult(
                success=True,
                fixed_code=fixed_code,
                fix_method="llm",
                error_type=error.error_type,
                message=f"Fixed using LLM ({tokens_used} tokens)",
                tokens_used=tokens_used
            )

        except Exception as e:
            logger.error(f"LLM fix failed: {e}")
            return FixResult(
                success=False,
                fixed_code=None,
                fix_method="llm",
                error_type=error.error_type,
                message=f"LLM fix failed: {str(e)}",
                tokens_used=0
            )

    def _build_minimal_prompt(self, code: str, error: ErrorInfo, component_name: str) -> str:
        """Build minimal prompt to reduce tokens"""

        # For JSX errors, only send problematic section
        if error.code_snippet:
            context = error.code_snippet
        else:
            # Send only last 500 chars if code is long
            context = code[-500:] if len(code) > 500 else code

        prompt = f"""Fix this React component error. Return ONLY the fixed code, no explanation.

Error: {error.message}
Component: {component_name}

Code:
```javascript
{context}
```

Return fixed code only:"""

        return prompt

    def _extract_code(self, response: str) -> str:
        """Extract code from LLM response"""
        # Try to extract from code block
        code_match = re.search(r'```(?:javascript|jsx|js)?\n(.*?)\n```', response, re.DOTALL)
        if code_match:
            return code_match.group(1)

        # Otherwise return full response
        return response.strip()


# ============================================================================
# MASTER ERROR HANDLER
# ============================================================================

class TemplateErrorHandler:
    """
    Master error handler - coordinates detection and fixing
    Strategy: Rule-based first (zero tokens) → LLM fallback (minimal tokens)
    """

    def __init__(self, use_llm_fallback: bool = True, use_haiku: bool = True):
        """
        Args:
            use_llm_fallback: Enable LLM fixes for complex errors
            use_haiku: Use Haiku instead of Sonnet for LLM fixes
        """
        self.detector = TemplateErrorDetector()
        self.rule_fixer = RuleBasedFixer()
        self.llm_fixer = LLMFixer(use_haiku=use_haiku) if use_llm_fallback else None

        # Statistics
        self.stats = {
            'total_errors_detected': 0,
            'rule_based_fixes': 0,
            'llm_fixes': 0,
            'unfixed_errors': 0,
            'total_tokens_used': 0
        }

    def validate_and_fix(self, code: str, component_name: str, max_iterations: int = 3) -> Tuple[bool, str, List[str]]:
        """
        Validate code and fix errors

        Args:
            code: Generated code
            component_name: Component name
            max_iterations: Max fix attempts

        Returns:
            (success, fixed_code, fix_messages)
        """
        current_code = code
        all_messages = []
        iteration = 0

        while iteration < max_iterations:
            iteration += 1

            # Detect errors
            errors = self.detector.detect_errors(current_code, component_name)

            if not errors:
                # No errors found!
                return (True, current_code, all_messages)

            self.stats['total_errors_detected'] += len(errors)
            logger.info(f"Iteration {iteration}: Found {len(errors)} errors")

            # Try to fix each error
            fixed_any = False

            for error in errors:
                # Try rule-based fix first
                fix_result = self.rule_fixer.fix_error(current_code, error, component_name)

                if fix_result and fix_result.success:
                    current_code = fix_result.fixed_code
                    self.stats['rule_based_fixes'] += 1
                    all_messages.append(f"✅ {fix_result.message}")
                    fixed_any = True
                    logger.info(f"Rule-based fix: {fix_result.message}")

                # If rules failed, try LLM
                elif self.llm_fixer:
                    logger.info(f"Attempting LLM fix for {error.error_type.value}")
                    fix_result = self.llm_fixer.fix_error(current_code, error, component_name)

                    if fix_result.success:
                        current_code = fix_result.fixed_code
                        self.stats['llm_fixes'] += 1
                        self.stats['total_tokens_used'] += fix_result.tokens_used
                        all_messages.append(f"✅ {fix_result.message}")
                        fixed_any = True
                        logger.info(f"LLM fix: {fix_result.message}")
                    else:
                        self.stats['unfixed_errors'] += 1
                        all_messages.append(f"❌ Could not fix: {error.message}")
                        logger.warning(f"Could not fix: {error.message}")
                else:
                    self.stats['unfixed_errors'] += 1
                    all_messages.append(f"❌ No fix available: {error.message}")

            # If we didn't fix anything, break
            if not fixed_any:
                break

        # Final check
        final_errors = self.detector.detect_errors(current_code, component_name)

        if not final_errors:
            return (True, current_code, all_messages)
        else:
            return (False, current_code, all_messages)

    def get_stats(self) -> Dict:
        """Get error handling statistics"""
        return {
            **self.stats,
            'llm_tokens_used': self.llm_fixer.total_tokens_used if self.llm_fixer else 0
        }

    def print_stats(self):
        """Print error handling statistics"""
        logger.info("=" * 60)
        logger.info("ERROR HANDLING STATISTICS")
        logger.info("=" * 60)
        logger.info(f"Total errors detected: {self.stats['total_errors_detected']}")
        logger.info(f"Fixed by rules: {self.stats['rule_based_fixes']} (0 tokens)")
        logger.info(f"Fixed by LLM: {self.stats['llm_fixes']} ({self.stats['total_tokens_used']} tokens)")
        logger.info(f"Unfixed errors: {self.stats['unfixed_errors']}")
        logger.info(f"Total tokens used: {self.stats['total_tokens_used']}")
        logger.info("=" * 60)
