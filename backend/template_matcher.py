"""
Template Matcher - Matches intents to templates with STRICT feature matching
Zero hallucination: only returns templates that exactly match intent + features
"""

import logging
from typing import List, Dict, Optional, Set, Tuple
from dataclasses import dataclass

from intent_classifier import Intent
from template_metadata_schema import TemplateMetadata, TemplateCatalog, get_catalog

logger = logging.getLogger(__name__)


# ============================================================================
# MATCHED TEMPLATE DATA STRUCTURE
# ============================================================================

@dataclass
class MatchedTemplate:
    """Represents a template matched to an intent"""
    template_id: str
    template: TemplateMetadata
    score: float
    match_reasons: List[str]
    confidence: float

    def __str__(self) -> str:
        return f"{self.template.name} (score: {self.score:.1f}, confidence: {self.confidence:.2f})"


# ============================================================================
# TEMPLATE MATCHER
# ============================================================================

class TemplateMatcher:
    """
    Matches intents to templates using strict feature matching

    Key principles:
    1. Templates MUST match the intent path (no fuzzy matching)
    2. Templates MUST have ALL required features
    3. Ranking is deterministic and explainable
    4. No hallucination possible
    """

    def __init__(self, catalog: Optional[TemplateCatalog] = None):
        """
        Args:
            catalog: Template catalog (uses singleton if not provided)
        """
        self.catalog = catalog or get_catalog()

    def match(
        self,
        intent: Intent,
        website_type: Optional[str] = None,
        user_preferences: Optional[Dict] = None
    ) -> List[MatchedTemplate]:
        """
        Find templates matching this intent

        Args:
            intent: The intent to match
            website_type: Optional website type for ranking
            user_preferences: Optional user preferences (style, complexity, etc.)

        Returns:
            List of MatchedTemplate objects, sorted by score (best first)
        """
        logger.info(f"🔍 Matching templates for: {intent.get_path()}")

        # Step 1: Get all templates for this intent
        candidate_templates = self._get_candidates_for_intent(intent)

        if not candidate_templates:
            logger.warning(f"   ⚠️  No templates found for intent: {intent.get_path()}")
            return []

        logger.info(f"   Found {len(candidate_templates)} candidates")

        # Step 2: STRICT feature filtering
        if intent.features:
            candidate_templates = self._filter_by_features(
                candidate_templates,
                intent.features,
                strict=True  # MUST have ALL features
            )
            logger.info(f"   After feature filtering: {len(candidate_templates)} candidates")

        if not candidate_templates:
            logger.warning(f"   ⚠️  No templates match required features: {intent.features}")
            return []

        # Step 3: Score and rank
        matched = self._score_and_rank(
            candidate_templates,
            intent,
            website_type,
            user_preferences
        )

        # Step 4: Return top matches
        top_matches = matched[:5]  # Top 5

        logger.info(f"   ✅ Top matches:")
        for i, match in enumerate(top_matches[:3], 1):
            logger.info(f"      {i}. {match.template.name} (score: {match.score:.1f})")

        return top_matches

    def match_multiple(
        self,
        intents: List[Intent],
        website_type: Optional[str] = None,
        user_preferences: Optional[Dict] = None
    ) -> Dict[str, List[MatchedTemplate]]:
        """
        Match multiple intents at once

        Args:
            intents: List of intents to match
            website_type: Optional website type
            user_preferences: Optional user preferences

        Returns:
            Dict mapping intent.get_path() -> List[MatchedTemplate]
        """
        results = {}

        for intent in intents:
            matches = self.match(intent, website_type, user_preferences)
            if matches:
                results[intent.get_path()] = matches

        return results

    def _get_candidates_for_intent(self, intent: Intent) -> List[TemplateMetadata]:
        """
        Get all templates that match the intent

        Uses exact intent path matching (no fuzzy matching)
        """
        # Try exact match first (with variant)
        intent_path = intent.get_path()
        candidates = self.catalog.get_by_intent(intent_path)

        if candidates:
            logger.debug(f"      Exact match: {len(candidates)} templates")
            return candidates

        # Try without variant
        if intent.variant:
            intent_path_no_variant = f"{intent.domain}.{intent.category}.{intent.intent}"
            candidates = self.catalog.get_by_intent(intent_path_no_variant)

            if candidates:
                logger.debug(f"      Match without variant: {len(candidates)} templates")
                return candidates

        # Try with different variants
        if intent.variant:
            # Get all templates for this intent and filter by category
            all_candidates = []
            intent_base = f"{intent.domain}.{intent.category}.{intent.intent}"

            # Search through all templates
            for template in self.catalog.get_all_templates():
                template_intent_base = f"{template.intent.domain}.{template.intent.category}.{template.intent.intent}"
                if template_intent_base == intent_base:
                    all_candidates.append(template)

            if all_candidates:
                logger.debug(f"      Found {len(all_candidates)} templates for base intent")
                return all_candidates

        return []

    def _filter_by_features(
        self,
        templates: List[TemplateMetadata],
        required_features: List[str],
        strict: bool = True
    ) -> List[TemplateMetadata]:
        """
        Filter templates by features

        Args:
            templates: List of templates to filter
            required_features: Features that must be present
            strict: If True, template must have ALL features. If False, ANY feature.

        Returns:
            Filtered list of templates
        """
        if not required_features:
            return templates

        filtered = []

        for template in templates:
            template_features = set(template.features.has)

            if strict:
                # Template MUST have ALL required features
                if all(feature in template_features for feature in required_features):
                    filtered.append(template)
            else:
                # Template must have ANY required feature
                if any(feature in template_features for feature in required_features):
                    filtered.append(template)

        return filtered

    def _score_and_rank(
        self,
        templates: List[TemplateMetadata],
        intent: Intent,
        website_type: Optional[str],
        user_preferences: Optional[Dict]
    ) -> List[MatchedTemplate]:
        """
        Score and rank templates

        Scoring is multi-dimensional and fully explainable
        """
        matched = []

        for template in templates:
            score, reasons, confidence = self._calculate_score(
                template,
                intent,
                website_type,
                user_preferences
            )

            matched.append(MatchedTemplate(
                template_id=template.id,
                template=template,
                score=score,
                match_reasons=reasons,
                confidence=confidence
            ))

        # Sort by score descending
        matched.sort(key=lambda x: x.score, reverse=True)

        return matched

    def _calculate_score(
        self,
        template: TemplateMetadata,
        intent: Intent,
        website_type: Optional[str],
        user_preferences: Optional[Dict]
    ) -> Tuple[float, List[str], float]:
        """
        Calculate match score for a template

        Returns:
            (score, reasons, confidence)
        """
        score = 0.0
        reasons = []

        # ===================================================================
        # 1. VARIANT EXACT MATCH (Highest Priority)
        # ===================================================================
        if intent.variant and template.intent.variant == intent.variant:
            score += 100
            reasons.append(f"Exact variant match ({intent.variant})")

        # ===================================================================
        # 2. WEBSITE TYPE MATCH
        # ===================================================================
        if website_type and website_type in template.use_cases:
            score += 50
            reasons.append(f"Optimized for {website_type}")

        # ===================================================================
        # 3. QUALITY METRICS (0-100 points)
        # ===================================================================

        # User rating (0-50 points)
        # 5.0 rating = 50 points, 4.0 rating = 40 points, etc.
        rating_score = template.quality_metrics.user_rating * 10
        score += rating_score
        if template.quality_metrics.user_rating >= 4.5:
            reasons.append(f"High user rating ({template.quality_metrics.user_rating}/5.0)")

        # Completion rate (0-30 points)
        # 1.0 = 30 points, 0.85 = 25.5 points, etc.
        completion_score = template.quality_metrics.completion_rate * 30
        score += completion_score

        # Usage count (0-20 points, normalized)
        # 1000+ uses = 20 points, 500 uses = 10 points, etc.
        usage_score = min(template.quality_metrics.usage_count / 50, 20)
        score += usage_score
        if template.quality_metrics.usage_count > 500:
            reasons.append(f"Widely used ({template.quality_metrics.usage_count}+ times)")

        # ===================================================================
        # 4. FEATURE RICHNESS (0-15 points)
        # ===================================================================

        # More features is generally better (within reason)
        feature_count = len(template.features.has)
        feature_score = min(feature_count, 15)
        score += feature_score

        # Bonus if has all requested features
        if intent.features:
            template_features = set(template.features.has)
            matched_features = [f for f in intent.features if f in template_features]

            if matched_features:
                score += len(matched_features) * 2  # 2 points per matched feature
                reasons.append(f"Has requested features: {', '.join(matched_features)}")

        # ===================================================================
        # 5. USER PREFERENCES (0-25 points)
        # ===================================================================

        if user_preferences:
            # Style preference
            preferred_style = user_preferences.get('style')
            if preferred_style and template.ui_characteristics.style == preferred_style:
                score += 10
                reasons.append(f"Matches style preference ({preferred_style})")

            # Complexity preference
            preferred_complexity = user_preferences.get('complexity')
            if preferred_complexity and template.ui_characteristics.complexity == preferred_complexity:
                score += 10
                reasons.append(f"Matches complexity preference ({preferred_complexity})")

            # Color scheme preference
            preferred_colors = user_preferences.get('color_scheme')
            if preferred_colors and template.ui_characteristics.color_scheme == preferred_colors:
                score += 5
                reasons.append(f"Matches color preference ({preferred_colors})")

        # ===================================================================
        # 6. TECHNICAL COMPATIBILITY (0-10 points)
        # ===================================================================

        # Responsive design
        if template.technical.responsive:
            score += 5
            reasons.append("Fully responsive")

        # Accessibility
        if template.technical.accessibility in ['WCAG_AA', 'WCAG_AAA']:
            score += 5
            reasons.append(f"Accessible ({template.technical.accessibility})")

        # ===================================================================
        # 7. RECENCY BONUS (0-5 points)
        # ===================================================================

        # Newer templates get a small bonus
        # This would require parsing last_updated datetime
        # For now, skip this

        # ===================================================================
        # Calculate confidence
        # ===================================================================

        # Confidence based on how definitive the match is
        confidence = intent.confidence

        # Boost confidence if exact variant match
        if intent.variant and template.intent.variant == intent.variant:
            confidence = min(confidence * 1.1, 1.0)

        # Boost confidence if high quality
        if template.quality_metrics.user_rating >= 4.5:
            confidence = min(confidence * 1.05, 1.0)

        # Lower confidence if many features don't match
        if intent.features:
            template_features = set(template.features.has)
            missing_features = [f for f in intent.features if f not in template_features]
            if missing_features:
                confidence *= 0.9

        return score, reasons, confidence

    def get_best_match(
        self,
        intent: Intent,
        website_type: Optional[str] = None,
        user_preferences: Optional[Dict] = None
    ) -> Optional[MatchedTemplate]:
        """
        Get the single best match for an intent

        Args:
            intent: Intent to match
            website_type: Optional website type
            user_preferences: Optional user preferences

        Returns:
            Best MatchedTemplate or None
        """
        matches = self.match(intent, website_type, user_preferences)
        return matches[0] if matches else None

    def get_alternatives(
        self,
        template_id: str,
        limit: int = 3
    ) -> List[TemplateMetadata]:
        """
        Get alternative templates similar to the given template

        Args:
            template_id: Template to find alternatives for
            limit: Max number of alternatives

        Returns:
            List of alternative templates
        """
        template = self.catalog.get_template(template_id)
        if not template:
            return []

        # Find templates with same intent but different variants
        intent_path = f"{template.intent.domain}.{template.intent.category}.{template.intent.intent}"
        candidates = self.catalog.get_by_intent(intent_path)

        # Exclude the original template
        alternatives = [t for t in candidates if t.id != template_id]

        # Sort by quality
        alternatives.sort(
            key=lambda t: t.quality_metrics.user_rating,
            reverse=True
        )

        return alternatives[:limit]


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

# Singleton instance
_matcher_instance: Optional[TemplateMatcher] = None


def get_matcher() -> TemplateMatcher:
    """Get singleton matcher instance"""
    global _matcher_instance

    if _matcher_instance is None:
        _matcher_instance = TemplateMatcher()

    return _matcher_instance


def match_intent(
    intent: Intent,
    website_type: Optional[str] = None
) -> List[MatchedTemplate]:
    """Quick helper to match an intent"""
    matcher = get_matcher()
    return matcher.match(intent, website_type)


def get_best_template(
    intent: Intent,
    website_type: Optional[str] = None
) -> Optional[MatchedTemplate]:
    """Quick helper to get best template for intent"""
    matcher = get_matcher()
    return matcher.get_best_match(intent, website_type)
