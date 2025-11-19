"""
Prompt Enhancement System
Uses LLM to clarify vague prompts, extract requirements, and ask follow-up questions
Minimal tokens using smart prompting
"""

import os
import logging
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import json

logger = logging.getLogger(__name__)


# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class EnhancedPrompt:
    """Enhanced version of user's prompt with extracted details"""

    # Original
    original_prompt: str

    # Enhanced version
    enhanced_prompt: str

    # Extracted details
    primary_goal: str
    target_audience: str
    key_features: List[str]
    business_model: Optional[str]  # "e-commerce", "subscription", "free", etc.

    # Clarifications
    clarifying_questions: List[str]
    assumptions: List[str]

    # Confidence
    confidence_score: float  # 0.0 to 1.0
    needs_clarification: bool


@dataclass
class UserResponse:
    """User's response to clarifying questions"""
    answers: Dict[str, str]
    additional_context: Optional[str]


# ============================================================================
# PROMPT ENHANCER
# ============================================================================

class PromptEnhancer:
    """
    Enhances user prompts using LLM
    Uses minimal tokens with targeted prompts
    """

    def __init__(self, use_haiku: bool = True):
        """
        Args:
            use_haiku: Use Claude Haiku (cheaper) vs Sonnet
        """
        self.use_haiku = use_haiku
        self.model = "claude-haiku-3-5-20241022" if use_haiku else "claude-sonnet-4-5-20250929"
        self.total_tokens_used = 0

    def enhance_prompt(
        self,
        user_prompt: str,
        auto_clarify: bool = True
    ) -> EnhancedPrompt:
        """
        Enhance user's prompt with LLM

        Args:
            user_prompt: User's original prompt
            auto_clarify: If False, always ask questions. If True, make reasonable assumptions.

        Returns:
            EnhancedPrompt with extracted details
        """
        try:
            import anthropic

            client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

            # Build enhancement prompt
            enhancement_prompt = self._build_enhancement_prompt(user_prompt, auto_clarify)

            # Call LLM
            response = client.messages.create(
                model=self.model,
                max_tokens=800,  # Keep it concise
                messages=[{
                    "role": "user",
                    "content": enhancement_prompt
                }]
            )

            # Track tokens
            tokens_used = response.usage.input_tokens + response.usage.output_tokens
            self.total_tokens_used += tokens_used
            logger.info(f"Prompt enhancement used {tokens_used} tokens")

            # Parse response
            result = self._parse_enhancement_response(
                response.content[0].text,
                user_prompt
            )

            return result

        except Exception as e:
            logger.error(f"Prompt enhancement failed: {e}")
            # Fallback: return original prompt
            return EnhancedPrompt(
                original_prompt=user_prompt,
                enhanced_prompt=user_prompt,
                primary_goal="Create a website",
                target_audience="General public",
                key_features=[],
                business_model=None,
                clarifying_questions=[],
                assumptions=[],
                confidence_score=0.5,
                needs_clarification=False
            )

    def _build_enhancement_prompt(self, user_prompt: str, auto_clarify: bool) -> str:
        """Build minimal prompt for LLM"""

        if auto_clarify:
            mode_instruction = "Make reasonable assumptions for missing details."
        else:
            mode_instruction = "Ask clarifying questions for any ambiguities."

        return f"""Analyze this website request and extract structured information.

User's request: "{user_prompt}"

{mode_instruction}

Return JSON with:
{{
  "enhanced_prompt": "Detailed description of what they want",
  "primary_goal": "Main purpose (e.g., 'Sell gym accessories online')",
  "target_audience": "Who will use this (e.g., 'Gym members and fitness enthusiasts')",
  "key_features": ["Feature 1", "Feature 2", ...],
  "business_model": "e-commerce|subscription|free|lead-gen|portfolio",
  "clarifying_questions": ["Question 1?", "Question 2?"],
  "assumptions": ["Assumption 1", "Assumption 2"],
  "confidence_score": 0.0-1.0,
  "needs_clarification": true|false
}}

Focus on:
1. What are they building?
2. Who is it for?
3. What features are needed?
4. How will it make money (if applicable)?
5. What's unclear?

Return ONLY valid JSON:"""

    def _parse_enhancement_response(
        self,
        response_text: str,
        original_prompt: str
    ) -> EnhancedPrompt:
        """Parse LLM response into EnhancedPrompt"""

        try:
            # Extract JSON from response
            json_match = response_text.strip()
            if '```json' in json_match:
                json_match = json_match.split('```json')[1].split('```')[0].strip()
            elif '```' in json_match:
                json_match = json_match.split('```')[1].split('```')[0].strip()

            data = json.loads(json_match)

            return EnhancedPrompt(
                original_prompt=original_prompt,
                enhanced_prompt=data.get('enhanced_prompt', original_prompt),
                primary_goal=data.get('primary_goal', 'Create a website'),
                target_audience=data.get('target_audience', 'General public'),
                key_features=data.get('key_features', []),
                business_model=data.get('business_model'),
                clarifying_questions=data.get('clarifying_questions', []),
                assumptions=data.get('assumptions', []),
                confidence_score=data.get('confidence_score', 0.5),
                needs_clarification=data.get('needs_clarification', False)
            )

        except Exception as e:
            logger.error(f"Failed to parse enhancement response: {e}")
            # Return minimal enhancement
            return EnhancedPrompt(
                original_prompt=original_prompt,
                enhanced_prompt=original_prompt,
                primary_goal="Create a website",
                target_audience="General public",
                key_features=[],
                business_model=None,
                clarifying_questions=[],
                assumptions=[],
                confidence_score=0.3,
                needs_clarification=True
            )

    def refine_with_answers(
        self,
        enhanced_prompt: EnhancedPrompt,
        user_response: UserResponse
    ) -> EnhancedPrompt:
        """
        Refine enhancement based on user's answers to questions

        Args:
            enhanced_prompt: Original enhancement
            user_response: User's answers

        Returns:
            Refined EnhancedPrompt
        """
        try:
            import anthropic

            client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

            # Build refinement prompt
            refinement_prompt = self._build_refinement_prompt(
                enhanced_prompt,
                user_response
            )

            # Call LLM
            response = client.messages.create(
                model=self.model,
                max_tokens=500,
                messages=[{
                    "role": "user",
                    "content": refinement_prompt
                }]
            )

            # Track tokens
            tokens_used = response.usage.input_tokens + response.usage.output_tokens
            self.total_tokens_used += tokens_used
            logger.info(f"Prompt refinement used {tokens_used} tokens")

            # Parse refined response
            refined = self._parse_enhancement_response(
                response.content[0].text,
                enhanced_prompt.original_prompt
            )

            # Mark as clarified
            refined.needs_clarification = False
            refined.confidence_score = min(1.0, refined.confidence_score + 0.3)

            return refined

        except Exception as e:
            logger.error(f"Refinement failed: {e}")
            return enhanced_prompt

    def _build_refinement_prompt(
        self,
        enhanced: EnhancedPrompt,
        response: UserResponse
    ) -> str:
        """Build refinement prompt"""

        answers_text = "\n".join([
            f"Q: {q}\nA: {response.answers.get(q, 'No answer')}"
            for q in enhanced.clarifying_questions
        ])

        additional = f"\n\nAdditional context: {response.additional_context}" if response.additional_context else ""

        return f"""Refine this website specification based on user's answers.

Original request: "{enhanced.original_prompt}"

Previous analysis:
- Goal: {enhanced.primary_goal}
- Features: {', '.join(enhanced.key_features)}

User's answers:
{answers_text}{additional}

Return updated JSON with same structure but refined based on answers.
Return ONLY valid JSON:"""

    def get_stats(self) -> Dict:
        """Get token usage statistics"""
        return {
            'total_tokens_used': self.total_tokens_used,
            'model': self.model
        }


# ============================================================================
# INTERACTIVE CLARIFIER
# ============================================================================

class InteractiveClarifier:
    """
    Manages interactive clarification process
    Asks questions and collects answers
    """

    def __init__(self, enhancer: PromptEnhancer):
        self.enhancer = enhancer

    def clarify_interactively(
        self,
        user_prompt: str,
        max_rounds: int = 2
    ) -> EnhancedPrompt:
        """
        Run interactive clarification process

        Args:
            user_prompt: User's original prompt
            max_rounds: Maximum clarification rounds

        Returns:
            Final EnhancedPrompt
        """
        # Initial enhancement
        enhanced = self.enhancer.enhance_prompt(user_prompt, auto_clarify=False)

        round_num = 0
        while enhanced.needs_clarification and round_num < max_rounds:
            round_num += 1

            print(f"\n--- Clarification Round {round_num} ---\n")

            if not enhanced.clarifying_questions:
                break

            # Ask questions
            answers = self._ask_questions(enhanced.clarifying_questions)

            # Get additional context
            additional = input("\nAny additional details? (press Enter to skip): ").strip()

            # Create response
            user_response = UserResponse(
                answers=answers,
                additional_context=additional if additional else None
            )

            # Refine
            enhanced = self.enhancer.refine_with_answers(enhanced, user_response)

        return enhanced

    def _ask_questions(self, questions: List[str]) -> Dict[str, str]:
        """Ask user the clarifying questions"""
        answers = {}

        for i, question in enumerate(questions, 1):
            print(f"\n{i}. {question}")
            answer = input("   Answer: ").strip()
            if answer:
                answers[question] = answer

        return answers


# ============================================================================
# SMART PROMPT BUILDER
# ============================================================================

class SmartPromptBuilder:
    """
    Combines enhancement with project planning
    Creates optimized prompt for template selection
    """

    def __init__(self, enhancer: PromptEnhancer):
        self.enhancer = enhancer

    def build_smart_prompt(
        self,
        user_prompt: str,
        auto_clarify: bool = True
    ) -> Tuple[str, EnhancedPrompt]:
        """
        Build smart prompt for planning/generation

        Args:
            user_prompt: Original user prompt
            auto_clarify: Make assumptions vs ask questions

        Returns:
            (optimized_prompt, enhanced_prompt_object)
        """
        # Enhance prompt
        enhanced = self.enhancer.enhance_prompt(user_prompt, auto_clarify)

        # Build optimized prompt
        optimized = self._build_optimized_prompt(enhanced)

        return optimized, enhanced

    def _build_optimized_prompt(self, enhanced: EnhancedPrompt) -> str:
        """Build optimized prompt from enhancement"""

        # Start with enhanced description
        prompt_parts = [enhanced.enhanced_prompt]

        # Add specific requirements
        if enhanced.key_features:
            features_text = ", ".join(enhanced.key_features)
            prompt_parts.append(f"Required features: {features_text}")

        # Add target audience context
        if enhanced.target_audience != "General public":
            prompt_parts.append(f"Target audience: {enhanced.target_audience}")

        # Add business model context
        if enhanced.business_model:
            if enhanced.business_model == "e-commerce":
                prompt_parts.append("Include product catalog, shopping cart, checkout, and payment processing")
            elif enhanced.business_model == "subscription":
                prompt_parts.append("Include user accounts, subscription management, and recurring payments")
            elif enhanced.business_model == "lead-gen":
                prompt_parts.append("Include contact forms, newsletter signup, and lead capture")

        # Combine
        optimized_prompt = ". ".join(prompt_parts) + "."

        return optimized_prompt


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def print_enhancement(enhanced: EnhancedPrompt):
    """Pretty print enhancement results"""

    print("=" * 80)
    print("ENHANCED PROMPT ANALYSIS")
    print("=" * 80)
    print()

    print(f"Original Prompt:")
    print(f'  "{enhanced.original_prompt}"')
    print()

    print(f"Enhanced Version:")
    print(f'  "{enhanced.enhanced_prompt}"')
    print()

    print(f"Primary Goal:")
    print(f"  {enhanced.primary_goal}")
    print()

    print(f"Target Audience:")
    print(f"  {enhanced.target_audience}")
    print()

    if enhanced.key_features:
        print("Key Features:")
        for feature in enhanced.key_features:
            print(f"  • {feature}")
        print()

    if enhanced.business_model:
        print(f"Business Model: {enhanced.business_model}")
        print()

    if enhanced.assumptions:
        print("Assumptions Made:")
        for assumption in enhanced.assumptions:
            print(f"  • {assumption}")
        print()

    if enhanced.clarifying_questions:
        print("Clarifying Questions:")
        for i, question in enumerate(enhanced.clarifying_questions, 1):
            print(f"  {i}. {question}")
        print()

    print(f"Confidence: {enhanced.confidence_score * 100:.0f}%")
    print(f"Needs Clarification: {'Yes' if enhanced.needs_clarification else 'No'}")
    print()
    print("=" * 80)


def quick_enhance(user_prompt: str) -> Tuple[str, EnhancedPrompt]:
    """
    Quick enhancement without interaction

    Args:
        user_prompt: User's original prompt

    Returns:
        (optimized_prompt, enhancement)
    """
    enhancer = PromptEnhancer(use_haiku=True)
    builder = SmartPromptBuilder(enhancer)

    optimized, enhanced = builder.build_smart_prompt(user_prompt, auto_clarify=True)

    return optimized, enhanced
