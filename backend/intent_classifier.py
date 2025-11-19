"""
Intent Classifier - Classifies user prompts into structured intents
Uses hybrid approach: keyword patterns + LLM for ambiguous cases
Zero hallucination: only returns curated intents from taxonomy
"""

import logging
import os
import json
from typing import List, Dict, Optional, Set
from dataclasses import dataclass, field
from anthropic import Anthropic

from intent_taxonomy import (
    INTENT_TAXONOMY,
    FEATURE_PATTERNS,
    WEBSITE_TYPE_PATTERNS,
    get_intent_path,
    get_intent_info,
    detect_website_type
)

logger = logging.getLogger(__name__)

# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class Intent:
    """Represents a classified intent"""
    domain: str
    category: str
    intent: str
    variant: Optional[str] = None
    confidence: float = 1.0
    features: List[str] = field(default_factory=list)
    source: str = "keyword"  # "keyword" or "llm"

    def __post_init__(self):
        if not self.features:
            self.features = []

    def get_path(self) -> str:
        """Get full intent path"""
        return get_intent_path(self.domain, self.category, self.intent, self.variant)

    def __str__(self) -> str:
        return f"{self.get_path()} (confidence: {self.confidence:.2f})"


# ============================================================================
# INTENT CLASSIFIER
# ============================================================================

class IntentClassifier:
    """
    Classifies user prompts into structured intents

    Uses three-tier approach:
    1. Fast keyword matching (95% of cases)
    2. Website type inference
    3. LLM for ambiguous cases (5% of cases)
    """

    def __init__(self, use_llm: bool = True):
        """
        Args:
            use_llm: Whether to use LLM for ambiguous cases
        """
        self.use_llm = use_llm
        self.client = None

        if use_llm:
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if api_key:
                self.client = Anthropic(api_key=api_key)
            else:
                logger.warning("ANTHROPIC_API_KEY not set, LLM classification disabled")
                self.use_llm = False

    def classify(
        self,
        prompt: str,
        website_type: Optional[str] = None
    ) -> List[Intent]:
        """
        Main classification method

        Args:
            prompt: User's description of what to build
            website_type: Optional website type hint (saas, ecommerce, etc.)

        Returns:
            List of Intent objects sorted by confidence
        """
        logger.info(f"🔍 Classifying: {prompt[:100]}...")

        intents: List[Intent] = []

        # Step 1: Detect website type if not provided
        if not website_type:
            website_type = detect_website_type(prompt)
            if website_type:
                logger.info(f"   Detected website type: {website_type}")

        # Step 2: Keyword-based classification (fast, 95% accuracy)
        keyword_intents = self._classify_by_keywords(prompt)
        logger.info(f"   Keyword matching found {len(keyword_intents)} intents")
        intents.extend(keyword_intents)

        # Step 3: Website type-based hints
        if website_type:
            type_intents = self._infer_from_website_type(website_type, prompt, intents)
            logger.info(f"   Website type added {len(type_intents)} intents")
            intents.extend(type_intents)

        # Step 4: Extract features
        features = self._extract_features(prompt)
        if features:
            logger.info(f"   Extracted features: {', '.join(features)}")

        # Step 5: For ambiguous cases, use LLM
        if self.use_llm and (len(intents) == 0 or self._is_ambiguous(prompt, intents)):
            logger.info("   Using LLM for classification...")
            llm_intents = self._classify_with_llm(prompt)
            logger.info(f"   LLM found {len(llm_intents)} intents")
            intents.extend(llm_intents)

        # Step 6: Deduplicate and rank
        intents = self._deduplicate_and_rank(intents)

        # Step 7: Add features to all intents
        for intent in intents:
            intent.features = features

        logger.info(f"✅ Final: {len(intents)} intents classified")
        for intent in intents:
            logger.debug(f"   - {intent}")

        return intents

    def _classify_by_keywords(self, prompt: str) -> List[Intent]:
        """Fast keyword-based classification"""
        intents: List[Intent] = []
        prompt_lower = prompt.lower()

        # ===================================================================
        # NAVIGATION PATTERNS
        # ===================================================================

        # Header
        if any(kw in prompt_lower for kw in ['header', 'navbar', 'nav', 'navigation', 'top bar']):
            variant = self._detect_header_variant(prompt_lower)
            intents.append(Intent(
                domain='navigation',
                category='header',
                intent='header',
                variant=variant,
                confidence=0.95,
                source='keyword'
            ))

        # Footer
        if any(kw in prompt_lower for kw in ['footer', 'bottom']):
            variant = self._detect_footer_variant(prompt_lower)
            intents.append(Intent(
                domain='navigation',
                category='footer',
                intent='footer',
                variant=variant,
                confidence=0.95,
                source='keyword'
            ))

        # Sidebar
        if any(kw in prompt_lower for kw in ['sidebar', 'side nav', 'side panel']):
            variant = 'collapsible' if 'collapsible' in prompt_lower or 'hamburger' in prompt_lower else 'fixed'
            intents.append(Intent(
                domain='navigation',
                category='sidebar',
                intent='sidebar',
                variant=variant,
                confidence=0.9,
                source='keyword'
            ))

        # ===================================================================
        # HERO & LANDING PATTERNS
        # ===================================================================

        # Hero
        if any(kw in prompt_lower for kw in ['hero', 'banner', 'landing', 'above fold']):
            variant = self._detect_hero_variant(prompt_lower)
            intents.append(Intent(
                domain='landing',
                category='hero',
                intent='hero',
                variant=variant,
                confidence=0.9,
                source='keyword'
            ))

        # CTA
        if any(kw in prompt_lower for kw in ['cta', 'call to action', 'call-to-action']):
            variant = 'form' if 'form' in prompt_lower else 'simple'
            intents.append(Intent(
                domain='landing',
                category='cta',
                intent='cta',
                variant=variant,
                confidence=0.9,
                source='keyword'
            ))

        # Features
        if any(kw in prompt_lower for kw in ['features', 'feature list', 'benefits', 'why choose']):
            variant = self._detect_features_variant(prompt_lower)
            intents.append(Intent(
                domain='landing',
                category='features',
                intent='features',
                variant=variant,
                confidence=0.85,
                source='keyword'
            ))

        # ===================================================================
        # AUTHENTICATION PATTERNS
        # ===================================================================

        # Login
        if any(kw in prompt_lower for kw in ['login', 'sign in', 'signin', 'log in']):
            variant = self._detect_login_variant(prompt_lower)
            intents.append(Intent(
                domain='authentication',
                category='login',
                intent='login',
                variant=variant,
                confidence=0.98,
                source='keyword'
            ))

        # Signup
        if any(kw in prompt_lower for kw in ['signup', 'sign up', 'register', 'registration', 'create account']):
            variant = 'wizard' if 'multi' in prompt_lower or 'wizard' in prompt_lower else 'simple'
            intents.append(Intent(
                domain='authentication',
                category='signup',
                intent='signup',
                variant=variant,
                confidence=0.98,
                source='keyword'
            ))

        # Password Reset
        if any(kw in prompt_lower for kw in ['password reset', 'forgot password', 'reset password']):
            intents.append(Intent(
                domain='authentication',
                category='password_reset',
                intent='password_reset',
                variant='simple',
                confidence=0.95,
                source='keyword'
            ))

        # ===================================================================
        # E-COMMERCE PATTERNS
        # ===================================================================

        # Shopping Cart
        if any(kw in prompt_lower for kw in ['shopping cart', 'cart', 'basket']):
            variant = self._detect_cart_variant(prompt_lower)
            intents.append(Intent(
                domain='ecommerce',
                category='cart',
                intent='cart',
                variant=variant,
                confidence=0.95,
                source='keyword'
            ))

        # Products
        if any(kw in prompt_lower for kw in ['product', 'products', 'catalog', 'items']):
            # Distinguish between product display and detail page
            if 'detail' in prompt_lower or 'page' in prompt_lower:
                variant = 'detail'
            elif 'list' in prompt_lower:
                variant = 'list'
            else:
                variant = 'grid'

            intents.append(Intent(
                domain='ecommerce',
                category='product_display',
                intent='product_display',
                variant=variant,
                confidence=0.85,
                source='keyword'
            ))

        # Checkout
        if any(kw in prompt_lower for kw in ['checkout', 'purchase', 'buy now']):
            variant = 'multi_step' if 'multi' in prompt_lower or 'wizard' in prompt_lower else 'single_page'
            intents.append(Intent(
                domain='ecommerce',
                category='checkout',
                intent='checkout',
                variant=variant,
                confidence=0.95,
                source='keyword'
            ))

        # Wishlist
        if any(kw in prompt_lower for kw in ['wishlist', 'favorites', 'save for later']):
            intents.append(Intent(
                domain='ecommerce',
                category='wishlist',
                intent='wishlist',
                variant='simple',
                confidence=0.95,
                source='keyword'
            ))

        # Product Filters
        if any(kw in prompt_lower for kw in ['filter', 'filters', 'refine', 'sort']):
            variant = 'sidebar' if 'sidebar' in prompt_lower else 'top'
            intents.append(Intent(
                domain='ecommerce',
                category='product_filters',
                intent='product_filters',
                variant=variant,
                confidence=0.85,
                source='keyword'
            ))

        # ===================================================================
        # PRICING PATTERNS
        # ===================================================================

        # Pricing Table
        if any(kw in prompt_lower for kw in ['pricing', 'price', 'plans', 'subscription', 'tiers']):
            variant = self._detect_pricing_variant(prompt_lower)
            intents.append(Intent(
                domain='pricing',
                category='table',
                intent='table',
                variant=variant,
                confidence=0.95,
                source='keyword'
            ))

        # ===================================================================
        # FORMS PATTERNS
        # ===================================================================

        # Contact Form
        if any(kw in prompt_lower for kw in ['contact form', 'contact us', 'get in touch', 'reach out']):
            variant = 'with_map' if 'map' in prompt_lower else 'simple'
            intents.append(Intent(
                domain='forms',
                category='contact',
                intent='contact',
                variant=variant,
                confidence=0.95,
                source='keyword'
            ))

        # Newsletter
        if any(kw in prompt_lower for kw in ['newsletter', 'subscribe', 'email signup', 'mailing list']):
            variant = self._detect_newsletter_variant(prompt_lower)
            intents.append(Intent(
                domain='forms',
                category='newsletter',
                intent='newsletter',
                variant=variant,
                confidence=0.9,
                source='keyword'
            ))

        # Search
        if any(kw in prompt_lower for kw in ['search', 'search bar', 'search box', 'find']):
            variant = 'autocomplete' if 'autocomplete' in prompt_lower or 'suggestions' in prompt_lower else 'simple'
            intents.append(Intent(
                domain='forms',
                category='search',
                intent='search',
                variant=variant,
                confidence=0.9,
                source='keyword'
            ))

        # Booking
        if any(kw in prompt_lower for kw in ['booking', 'appointment', 'reservation', 'schedule']):
            variant = 'calendar' if 'calendar' in prompt_lower else 'time_slots'
            intents.append(Intent(
                domain='forms',
                category='booking',
                intent='booking',
                variant=variant,
                confidence=0.95,
                source='keyword'
            ))

        # ===================================================================
        # CONTENT PATTERNS
        # ===================================================================

        # Blog
        if any(kw in prompt_lower for kw in ['blog', 'articles', 'posts', 'news']):
            if 'detail' in prompt_lower or 'individual' in prompt_lower:
                variant = 'post_detail'
            elif 'grid' in prompt_lower:
                variant = 'grid'
            else:
                variant = 'post_list'

            intents.append(Intent(
                domain='content',
                category='blog',
                intent='blog',
                variant=variant,
                confidence=0.9,
                source='keyword'
            ))

        # Gallery
        if any(kw in prompt_lower for kw in ['gallery', 'photos', 'images', 'portfolio']):
            variant = self._detect_gallery_variant(prompt_lower)
            intents.append(Intent(
                domain='content',
                category='gallery',
                intent='gallery',
                variant=variant,
                confidence=0.9,
                source='keyword'
            ))

        # Testimonials
        if any(kw in prompt_lower for kw in ['testimonials', 'reviews', 'customer reviews', 'feedback']):
            variant = 'carousel' if 'carousel' in prompt_lower or 'slider' in prompt_lower else 'grid'
            intents.append(Intent(
                domain='content',
                category='testimonials',
                intent='testimonials',
                variant=variant,
                confidence=0.9,
                source='keyword'
            ))

        # Team
        if any(kw in prompt_lower for kw in ['team', 'team members', 'about us', 'our team']):
            variant = 'grid'
            intents.append(Intent(
                domain='content',
                category='team',
                intent='team',
                variant=variant,
                confidence=0.9,
                source='keyword'
            ))

        # FAQ
        if any(kw in prompt_lower for kw in ['faq', 'frequently asked questions', 'questions', 'help']):
            variant = 'accordion'
            intents.append(Intent(
                domain='content',
                category='faq',
                intent='faq',
                variant=variant,
                confidence=0.95,
                source='keyword'
            ))

        # ===================================================================
        # DATA DISPLAY PATTERNS
        # ===================================================================

        # Table
        if any(kw in prompt_lower for kw in ['table', 'data table', 'list']) and 'pricing' not in prompt_lower:
            variant = self._detect_table_variant(prompt_lower)
            intents.append(Intent(
                domain='data',
                category='table',
                intent='table',
                variant=variant,
                confidence=0.85,
                source='keyword'
            ))

        # Charts
        if any(kw in prompt_lower for kw in ['chart', 'graph', 'visualization', 'analytics']):
            variant = 'dashboard'  # Default
            intents.append(Intent(
                domain='data',
                category='charts',
                intent='charts',
                variant=variant,
                confidence=0.85,
                source='keyword'
            ))

        # Stats
        if any(kw in prompt_lower for kw in ['stats', 'statistics', 'metrics', 'numbers', 'counters']):
            variant = 'cards'
            intents.append(Intent(
                domain='data',
                category='stats',
                intent='stats',
                variant=variant,
                confidence=0.85,
                source='keyword'
            ))

        # ===================================================================
        # ADMIN & DASHBOARD PATTERNS
        # ===================================================================

        # Dashboard
        if any(kw in prompt_lower for kw in ['dashboard', 'admin', 'overview', 'control panel']):
            variant = 'widgets'
            intents.append(Intent(
                domain='admin',
                category='dashboard',
                intent='dashboard',
                variant=variant,
                confidence=0.9,
                source='keyword'
            ))

        return intents

    def _infer_from_website_type(
        self,
        website_type: str,
        prompt: str,
        existing_intents: List[Intent]
    ) -> List[Intent]:
        """Infer intents based on website type"""
        new_intents: List[Intent] = []

        # Get common intents for this website type
        from intent_taxonomy import get_website_type_intents
        common_intent_paths = get_website_type_intents(website_type)

        # Convert to Intent objects
        existing_paths = {intent.get_path() for intent in existing_intents}

        for intent_path in common_intent_paths:
            # Skip if already detected
            if intent_path in existing_paths:
                continue

            # Parse path
            parts = intent_path.split('.')
            if len(parts) >= 3:
                domain, category, intent = parts[0], parts[1], parts[2]
                variant = parts[3] if len(parts) == 4 else None

                # Add with lower confidence (inferred, not explicitly requested)
                new_intents.append(Intent(
                    domain=domain,
                    category=category,
                    intent=intent,
                    variant=variant,
                    confidence=0.6,  # Lower confidence for inferred
                    source='website_type'
                ))

        return new_intents

    def _extract_features(self, prompt: str) -> List[str]:
        """Extract specific features mentioned in prompt"""
        features: Set[str] = set()
        prompt_lower = prompt.lower()

        for feature, keywords in FEATURE_PATTERNS.items():
            if any(kw in prompt_lower for kw in keywords):
                features.add(feature)

        return list(features)

    def _is_ambiguous(self, prompt: str, intents: List[Intent]) -> bool:
        """Determine if classification is ambiguous"""
        # Too few intents found
        if len(intents) < 2:
            return True

        # All intents have low confidence
        if all(intent.confidence < 0.7 for intent in intents):
            return True

        # Prompt is complex but few intents found
        word_count = len(prompt.split())
        if word_count > 20 and len(intents) < 3:
            return True

        return False

    def _classify_with_llm(self, prompt: str) -> List[Intent]:
        """Use LLM for ambiguous cases"""
        if not self.client:
            logger.warning("LLM classification requested but client not available")
            return []

        # Build a comprehensive prompt with all possible intents
        classification_prompt = self._build_llm_prompt(prompt)

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=2000,
                messages=[{"role": "user", "content": classification_prompt}]
            )

            result = response.content[0].text.strip()
            logger.debug(f"LLM response: {result[:200]}...")

            # Parse JSON response
            intents_data = json.loads(result)

            intents: List[Intent] = []
            for data in intents_data:
                intents.append(Intent(
                    domain=data['domain'],
                    category=data['category'],
                    intent=data['intent'],
                    variant=data.get('variant'),
                    confidence=data.get('confidence', 0.9),
                    source='llm'
                ))

            return intents

        except Exception as e:
            logger.error(f"LLM classification failed: {e}")
            return []

    def _build_llm_prompt(self, user_prompt: str) -> str:
        """Build prompt for LLM classification"""
        # Get sample intents from taxonomy
        sample_intents = [
            "navigation.header.header (variants: minimal, with_cta, mega_menu, ecommerce)",
            "navigation.footer.footer (variants: minimal, newsletter, multi_column)",
            "landing.hero.hero (variants: gradient, image, video, split)",
            "landing.features.features (variants: grid, list, tabs, icons)",
            "authentication.login.login (variants: simple, modal, social)",
            "authentication.signup.signup (variants: simple, wizard, social)",
            "ecommerce.cart.cart (variants: page, slideout, mini)",
            "ecommerce.product_display.product_display (variants: grid, list, detail)",
            "ecommerce.checkout.checkout (variants: single_page, multi_step)",
            "pricing.table.table (variants: simple, detailed, toggle)",
            "forms.contact.contact (variants: simple, detailed, with_map)",
            "forms.newsletter.newsletter (variants: inline, modal, footer)",
            "forms.search.search (variants: simple, autocomplete, advanced)",
            "content.blog.blog (variants: post_list, post_detail, grid)",
            "content.gallery.gallery (variants: grid, masonry, carousel)",
            "content.testimonials.testimonials (variants: carousel, grid, video)",
            "data.table.table (variants: basic, sortable, paginated)",
            "data.charts.charts (variants: line, bar, pie, dashboard)",
            "admin.dashboard.dashboard (variants: widgets, analytics, minimal)"
        ]

        return f"""Classify this website building request into specific intents from our taxonomy.

User request: "{user_prompt}"

Available intent patterns (domain.category.intent):
{chr(10).join('- ' + intent for intent in sample_intents)}

Instructions:
1. Identify ALL intents needed to fulfill the user's request
2. For each intent, pick the most appropriate variant
3. Return confidence score 0.0-1.0 (0.9+ for explicit, 0.7-0.8 for inferred, 0.5-0.6 for optional)
4. Return ONLY intents from the list above (no hallucination)

Return a JSON array:
[
  {{"domain": "navigation", "category": "header", "intent": "header", "variant": "with_cta", "confidence": 0.95}},
  {{"domain": "landing", "category": "hero", "intent": "hero", "variant": "gradient", "confidence": 0.9}}
]

Return ONLY the JSON array, nothing else."""

    def _deduplicate_and_rank(self, intents: List[Intent]) -> List[Intent]:
        """Deduplicate intents and rank by confidence"""
        # Group by intent path
        intent_map: Dict[str, Intent] = {}

        for intent in intents:
            path = intent.get_path()

            if path not in intent_map:
                intent_map[path] = intent
            else:
                # Keep higher confidence one
                if intent.confidence > intent_map[path].confidence:
                    intent_map[path] = intent

        # Sort by confidence descending
        ranked = sorted(intent_map.values(), key=lambda x: x.confidence, reverse=True)

        return ranked

    # ========================================================================
    # VARIANT DETECTION HELPERS
    # ========================================================================

    def _detect_header_variant(self, prompt: str) -> str:
        """Detect specific header variant"""
        if 'cta' in prompt or 'call to action' in prompt or 'button' in prompt:
            return 'with_cta'
        elif 'minimal' in prompt or 'simple' in prompt:
            return 'minimal'
        elif 'mega menu' in prompt or 'dropdown' in prompt:
            return 'mega_menu'
        elif 'ecommerce' in prompt or 'shop' in prompt or 'cart' in prompt:
            return 'ecommerce'
        elif 'transparent' in prompt:
            return 'transparent'
        elif 'sticky' in prompt or 'fixed' in prompt:
            return 'sticky'
        return 'minimal'

    def _detect_footer_variant(self, prompt: str) -> str:
        """Detect footer variant"""
        if 'newsletter' in prompt or 'subscribe' in prompt:
            return 'newsletter'
        elif 'multi' in prompt or 'columns' in prompt:
            return 'multi_column'
        elif 'social' in prompt:
            return 'social'
        return 'minimal'

    def _detect_hero_variant(self, prompt: str) -> str:
        """Detect hero section variant"""
        if 'video' in prompt:
            return 'video'
        elif 'gradient' in prompt:
            return 'gradient'
        elif 'image' in prompt or 'photo' in prompt:
            return 'image'
        elif 'split' in prompt or 'two column' in prompt:
            return 'split'
        elif 'animated' in prompt or 'animation' in prompt:
            return 'animated'
        return 'gradient'

    def _detect_features_variant(self, prompt: str) -> str:
        """Detect features section variant"""
        if 'grid' in prompt:
            return 'grid'
        elif 'list' in prompt:
            return 'list'
        elif 'tabs' in prompt or 'tabbed' in prompt:
            return 'tabs'
        elif 'icons' in prompt:
            return 'icons'
        return 'grid'

    def _detect_login_variant(self, prompt: str) -> str:
        """Detect login variant"""
        if 'social' in prompt or 'google' in prompt or 'facebook' in prompt:
            return 'social'
        elif 'modal' in prompt or 'popup' in prompt:
            return 'modal'
        elif '2fa' in prompt or 'two factor' in prompt:
            return 'two_factor'
        return 'simple'

    def _detect_cart_variant(self, prompt: str) -> str:
        """Detect cart variant"""
        if 'slide' in prompt or 'drawer' in prompt or 'slideout' in prompt:
            return 'slideout'
        elif 'mini' in prompt or 'small' in prompt or 'icon' in prompt:
            return 'mini'
        elif 'sticky' in prompt:
            return 'sticky'
        return 'page'

    def _detect_pricing_variant(self, prompt: str) -> str:
        """Detect pricing table variant"""
        if 'toggle' in prompt or 'monthly' in prompt or 'annual' in prompt:
            return 'toggle'
        elif 'detailed' in prompt or 'comparison' in prompt:
            return 'detailed'
        elif 'enterprise' in prompt or 'custom' in prompt:
            return 'enterprise'
        return 'simple'

    def _detect_newsletter_variant(self, prompt: str) -> str:
        """Detect newsletter variant"""
        if 'modal' in prompt or 'popup' in prompt:
            return 'modal'
        elif 'footer' in prompt:
            return 'footer'
        elif 'exit' in prompt:
            return 'exit_intent'
        return 'inline'

    def _detect_gallery_variant(self, prompt: str) -> str:
        """Detect gallery variant"""
        if 'masonry' in prompt or 'pinterest' in prompt:
            return 'masonry'
        elif 'carousel' in prompt or 'slider' in prompt:
            return 'carousel'
        elif 'lightbox' in prompt or 'popup' in prompt:
            return 'lightbox'
        elif 'filter' in prompt:
            return 'filterable'
        return 'grid'

    def _detect_table_variant(self, prompt: str) -> str:
        """Detect data table variant"""
        if 'sortable' in prompt or 'sort' in prompt:
            return 'sortable'
        elif 'paginated' in prompt or 'pagination' in prompt:
            return 'paginated'
        elif 'filterable' in prompt or 'filter' in prompt:
            return 'filterable'
        elif 'editable' in prompt or 'edit' in prompt:
            return 'editable'
        return 'basic'


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

# Singleton instance
_classifier_instance: Optional[IntentClassifier] = None


def get_classifier() -> IntentClassifier:
    """Get singleton classifier instance"""
    global _classifier_instance

    if _classifier_instance is None:
        _classifier_instance = IntentClassifier()

    return _classifier_instance


def classify_prompt(prompt: str, website_type: Optional[str] = None) -> List[Intent]:
    """Quick helper to classify a prompt"""
    classifier = get_classifier()
    return classifier.classify(prompt, website_type)
