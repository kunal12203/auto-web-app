"""
Intent Taxonomy - Comprehensive classification system for template selection
Defines all possible intents, variants, and their relationships
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field

# ============================================================================
# INTENT TAXONOMY - Hierarchical Structure
# ============================================================================

INTENT_TAXONOMY = {
    # =======================================================================
    # 1. AUTHENTICATION & AUTHORIZATION
    # =======================================================================
    "authentication": {
        "login": {
            "description": "User wants to log into existing account",
            "variants": {
                "simple": "Basic email/password form",
                "modal": "Popup/modal login",
                "social": "Social login (Google, Facebook, etc.)",
                "magic_link": "Passwordless email login",
                "two_factor": "With 2FA support"
            },
            "keywords": ["login", "sign in", "signin", "log in", "authenticate"],
            "features": ["email_input", "password_input", "remember_me", "submit_button"]
        },
        "signup": {
            "description": "User wants to create new account",
            "variants": {
                "simple": "Basic registration form",
                "wizard": "Multi-step registration",
                "social": "Social signup",
                "email_verification": "With email verification flow"
            },
            "keywords": ["signup", "sign up", "register", "registration", "create account"],
            "features": ["email_input", "password_input", "confirm_password", "submit_button"]
        },
        "password_reset": {
            "description": "User forgot password and wants to reset",
            "variants": {
                "simple": "Email-based reset",
                "security_questions": "With security questions",
                "sms": "SMS-based reset"
            },
            "keywords": ["password reset", "forgot password", "reset password", "recover password"],
            "features": ["email_input", "submit_button"]
        },
        "profile_management": {
            "description": "User wants to view/edit profile",
            "variants": {
                "simple": "Basic profile page",
                "settings": "Detailed settings page",
                "avatar_upload": "With avatar/photo upload"
            },
            "keywords": ["profile", "account settings", "my account", "user profile"],
            "features": ["form_fields", "save_button", "avatar"]
        }
    },

    # =======================================================================
    # 2. NAVIGATION & LAYOUT
    # =======================================================================
    "navigation": {
        "header": {
            "description": "Top navigation bar",
            "variants": {
                "minimal": "Logo + simple nav links",
                "with_cta": "Nav + prominent CTA button",
                "mega_menu": "With dropdown mega menu",
                "sticky": "Sticky/fixed header",
                "transparent": "Transparent overlay header",
                "ecommerce": "With search + cart icon"
            },
            "keywords": ["header", "navbar", "navigation", "nav", "top bar", "menu"],
            "features": ["logo", "navigation_links", "mobile_menu"]
        },
        "footer": {
            "description": "Bottom page footer",
            "variants": {
                "minimal": "Simple links + copyright",
                "newsletter": "With newsletter signup",
                "multi_column": "Multiple link columns",
                "social": "With social media links"
            },
            "keywords": ["footer", "bottom", "site footer"],
            "features": ["links", "copyright"]
        },
        "sidebar": {
            "description": "Side navigation panel",
            "variants": {
                "fixed": "Fixed sidebar",
                "collapsible": "Collapsible/hamburger",
                "admin": "Admin dashboard sidebar",
                "blog": "Blog/content sidebar"
            },
            "keywords": ["sidebar", "side nav", "side panel"],
            "features": ["navigation_links", "toggle"]
        },
        "breadcrumbs": {
            "description": "Navigation breadcrumb trail",
            "variants": {
                "simple": "Text-based",
                "with_icons": "With icons",
                "dropdown": "With dropdown navigation"
            },
            "keywords": ["breadcrumbs", "breadcrumb", "navigation trail"],
            "features": ["links", "separator"]
        }
    },

    # =======================================================================
    # 3. HERO & LANDING SECTIONS
    # =======================================================================
    "landing": {
        "hero": {
            "description": "Main hero/banner section",
            "variants": {
                "gradient": "Gradient background",
                "image": "Image background",
                "video": "Video background",
                "split": "Split layout (text + image)",
                "animated": "With animations",
                "centered": "Centered content"
            },
            "keywords": ["hero", "banner", "landing", "above fold", "hero section"],
            "features": ["headline", "subheadline", "cta_button"]
        },
        "cta": {
            "description": "Call-to-action section",
            "variants": {
                "simple": "Simple CTA block",
                "form": "CTA with form",
                "countdown": "With countdown timer",
                "pricing": "With pricing info"
            },
            "keywords": ["cta", "call to action", "call-to-action"],
            "features": ["headline", "button"]
        },
        "features": {
            "description": "Feature showcase section",
            "variants": {
                "grid": "Grid layout",
                "list": "Vertical list",
                "tabs": "Tabbed features",
                "icons": "With icons",
                "images": "With images/screenshots"
            },
            "keywords": ["features", "feature list", "benefits", "why choose"],
            "features": ["feature_items", "icons"]
        }
    },

    # =======================================================================
    # 4. CONTENT DISPLAY
    # =======================================================================
    "content": {
        "blog": {
            "description": "Blog/article display",
            "variants": {
                "post_list": "List of blog posts",
                "post_detail": "Individual post page",
                "grid": "Blog grid layout",
                "masonry": "Masonry layout",
                "sidebar": "With sidebar"
            },
            "keywords": ["blog", "articles", "posts", "news"],
            "features": ["post_items", "pagination"]
        },
        "gallery": {
            "description": "Image/photo gallery",
            "variants": {
                "grid": "Grid layout",
                "masonry": "Masonry/Pinterest style",
                "carousel": "Image carousel/slider",
                "lightbox": "With lightbox popup",
                "filterable": "With category filters"
            },
            "keywords": ["gallery", "photos", "images", "portfolio"],
            "features": ["image_items", "modal"]
        },
        "testimonials": {
            "description": "Customer testimonials/reviews",
            "variants": {
                "carousel": "Rotating testimonials",
                "grid": "Grid of testimonials",
                "video": "Video testimonials",
                "stats": "With statistics"
            },
            "keywords": ["testimonials", "reviews", "customer reviews", "feedback"],
            "features": ["testimonial_items", "author_info"]
        },
        "team": {
            "description": "Team member showcase",
            "variants": {
                "grid": "Team member grid",
                "card": "Individual cards",
                "bio": "With detailed bios"
            },
            "keywords": ["team", "team members", "about us", "our team"],
            "features": ["member_items", "photo", "bio"]
        },
        "faq": {
            "description": "Frequently asked questions",
            "variants": {
                "accordion": "Accordion/collapsible",
                "grid": "Grid layout",
                "searchable": "With search"
            },
            "keywords": ["faq", "frequently asked questions", "questions", "help"],
            "features": ["question_items", "expandable"]
        }
    },

    # =======================================================================
    # 5. E-COMMERCE
    # =======================================================================
    "ecommerce": {
        "product_display": {
            "description": "Show products for sale",
            "variants": {
                "grid": "Product grid",
                "list": "Product list",
                "card": "Product cards",
                "detail": "Product detail page",
                "quick_view": "Quick view modal"
            },
            "keywords": ["product", "products", "shop", "catalog", "items"],
            "features": ["product_items", "images", "price"]
        },
        "cart": {
            "description": "Shopping cart",
            "variants": {
                "page": "Full page cart",
                "slideout": "Slide-out cart",
                "mini": "Mini cart dropdown",
                "sticky": "Sticky cart summary"
            },
            "keywords": ["cart", "shopping cart", "basket"],
            "features": ["cart_items", "quantity_selector", "remove_button", "total"]
        },
        "checkout": {
            "description": "Purchase checkout flow",
            "variants": {
                "single_page": "One-page checkout",
                "multi_step": "Multi-step wizard",
                "guest": "Guest checkout",
                "express": "Express checkout"
            },
            "keywords": ["checkout", "purchase", "buy", "payment"],
            "features": ["shipping_form", "payment_form", "order_summary"]
        },
        "product_filters": {
            "description": "Filter/search products",
            "variants": {
                "sidebar": "Sidebar filters",
                "top": "Top bar filters",
                "modal": "Filter modal",
                "faceted": "Faceted search"
            },
            "keywords": ["filter", "filters", "search", "refine"],
            "features": ["filter_options", "apply_button"]
        },
        "wishlist": {
            "description": "Save favorite products",
            "variants": {
                "simple": "Basic wishlist",
                "with_notes": "With notes/comments",
                "shareable": "Shareable wishlist"
            },
            "keywords": ["wishlist", "favorites", "save for later"],
            "features": ["product_items", "remove_button"]
        }
    },

    # =======================================================================
    # 6. PRICING & SUBSCRIPTIONS
    # =======================================================================
    "pricing": {
        "table": {
            "description": "Pricing comparison table",
            "variants": {
                "simple": "Basic 2-3 tiers",
                "detailed": "Detailed feature comparison",
                "toggle": "Monthly/annual toggle",
                "highlighted": "With recommended tier",
                "enterprise": "With custom/enterprise tier"
            },
            "keywords": ["pricing", "price", "plans", "subscription", "tiers"],
            "features": ["pricing_tiers", "features_list", "cta_buttons"]
        },
        "calculator": {
            "description": "Price calculator",
            "variants": {
                "slider": "Slider-based",
                "dropdown": "Dropdown selections",
                "dynamic": "Real-time calculation"
            },
            "keywords": ["calculator", "price calculator", "estimate"],
            "features": ["inputs", "calculation", "total_display"]
        }
    },

    # =======================================================================
    # 7. FORMS & INPUTS
    # =======================================================================
    "forms": {
        "contact": {
            "description": "Contact form",
            "variants": {
                "simple": "Name + email + message",
                "detailed": "With phone, subject, etc.",
                "multi_step": "Multi-step form",
                "with_map": "With location map"
            },
            "keywords": ["contact", "contact form", "get in touch", "reach out"],
            "features": ["name_input", "email_input", "message_input", "submit_button"]
        },
        "newsletter": {
            "description": "Newsletter signup",
            "variants": {
                "inline": "Inline input + button",
                "modal": "Popup modal",
                "footer": "Footer embedded",
                "exit_intent": "Exit intent popup"
            },
            "keywords": ["newsletter", "subscribe", "email signup", "mailing list"],
            "features": ["email_input", "submit_button"]
        },
        "search": {
            "description": "Search functionality",
            "variants": {
                "simple": "Basic search bar",
                "autocomplete": "With autocomplete",
                "advanced": "Advanced search with filters",
                "results": "Search results page"
            },
            "keywords": ["search", "search bar", "find"],
            "features": ["search_input", "search_button"]
        },
        "booking": {
            "description": "Appointment/booking form",
            "variants": {
                "calendar": "Calendar-based",
                "time_slots": "Time slot selection",
                "multi_step": "Multi-step booking"
            },
            "keywords": ["booking", "appointment", "reservation", "schedule"],
            "features": ["date_picker", "time_picker", "submit_button"]
        }
    },

    # =======================================================================
    # 8. DATA DISPLAY
    # =======================================================================
    "data": {
        "table": {
            "description": "Data table",
            "variants": {
                "basic": "Simple table",
                "sortable": "Sortable columns",
                "paginated": "With pagination",
                "filterable": "With filters",
                "responsive": "Mobile-responsive",
                "editable": "Inline editing"
            },
            "keywords": ["table", "data table", "list"],
            "features": ["table_rows", "columns"]
        },
        "charts": {
            "description": "Data visualization",
            "variants": {
                "line": "Line chart",
                "bar": "Bar chart",
                "pie": "Pie/donut chart",
                "area": "Area chart",
                "dashboard": "Multi-chart dashboard"
            },
            "keywords": ["chart", "graph", "visualization", "analytics"],
            "features": ["chart_canvas", "data_points"]
        },
        "stats": {
            "description": "Statistics/metrics display",
            "variants": {
                "cards": "Stat cards",
                "counters": "Animated counters",
                "comparison": "Comparison stats"
            },
            "keywords": ["stats", "statistics", "metrics", "numbers"],
            "features": ["stat_items", "numbers"]
        }
    },

    # =======================================================================
    # 9. ADMIN & DASHBOARD
    # =======================================================================
    "admin": {
        "dashboard": {
            "description": "Admin dashboard overview",
            "variants": {
                "widgets": "Widget-based",
                "analytics": "Analytics-focused",
                "minimal": "Minimal/clean"
            },
            "keywords": ["dashboard", "admin", "overview", "control panel"],
            "features": ["widgets", "charts", "stats"]
        },
        "user_management": {
            "description": "Manage users",
            "variants": {
                "list": "User list/table",
                "detail": "User detail page",
                "permissions": "Permission management"
            },
            "keywords": ["users", "user management", "manage users"],
            "features": ["user_table", "actions"]
        },
        "content_management": {
            "description": "Manage content/posts",
            "variants": {
                "list": "Content list",
                "editor": "Content editor",
                "media": "Media library"
            },
            "keywords": ["cms", "content management", "manage content"],
            "features": ["content_list", "editor"]
        }
    },

    # =======================================================================
    # 10. MODALS & OVERLAYS
    # =======================================================================
    "overlays": {
        "modal": {
            "description": "Modal/popup dialog",
            "variants": {
                "simple": "Basic modal",
                "form": "Form modal",
                "image": "Image modal",
                "video": "Video modal",
                "confirmation": "Confirmation dialog"
            },
            "keywords": ["modal", "popup", "dialog", "overlay"],
            "features": ["modal_container", "close_button", "content"]
        },
        "toast": {
            "description": "Notification toast",
            "variants": {
                "success": "Success message",
                "error": "Error message",
                "warning": "Warning message",
                "info": "Info message"
            },
            "keywords": ["toast", "notification", "alert", "message"],
            "features": ["message", "close_button"]
        },
        "tooltip": {
            "description": "Tooltip/popover",
            "variants": {
                "simple": "Basic tooltip",
                "rich": "Rich content tooltip",
                "help": "Help/info tooltip"
            },
            "keywords": ["tooltip", "popover", "hint"],
            "features": ["trigger", "content"]
        }
    },

    # =======================================================================
    # 11. LOADING & FEEDBACK
    # =======================================================================
    "feedback": {
        "loader": {
            "description": "Loading indicator",
            "variants": {
                "spinner": "Spinner",
                "progress_bar": "Progress bar",
                "skeleton": "Skeleton screen",
                "dots": "Animated dots"
            },
            "keywords": ["loading", "loader", "spinner", "progress"],
            "features": ["animation"]
        },
        "empty_state": {
            "description": "No data/empty state",
            "variants": {
                "illustration": "With illustration",
                "cta": "With call-to-action",
                "simple": "Simple message"
            },
            "keywords": ["empty", "no data", "no results"],
            "features": ["message", "illustration"]
        }
    }
}

# ============================================================================
# WEBSITE TYPE PATTERNS
# ============================================================================

WEBSITE_TYPE_PATTERNS = {
    "saas": {
        "common_intents": [
            "navigation.header.with_cta",
            "landing.hero.gradient",
            "landing.features.grid",
            "pricing.table.toggle",
            "content.testimonials.carousel",
            "forms.newsletter.inline",
            "authentication.signup.simple"
        ],
        "keywords": ["saas", "software", "platform", "service"]
    },
    "ecommerce": {
        "common_intents": [
            "navigation.header.ecommerce",
            "ecommerce.product_display.grid",
            "ecommerce.cart.slideout",
            "ecommerce.checkout.multi_step",
            "ecommerce.product_filters.sidebar",
            "ecommerce.wishlist.simple"
        ],
        "keywords": ["store", "shop", "ecommerce", "e-commerce", "buy", "sell"]
    },
    "portfolio": {
        "common_intents": [
            "navigation.header.minimal",
            "landing.hero.image",
            "content.gallery.masonry",
            "content.team.card",
            "forms.contact.simple"
        ],
        "keywords": ["portfolio", "showcase", "work", "projects"]
    },
    "blog": {
        "common_intents": [
            "navigation.header.minimal",
            "content.blog.post_list",
            "navigation.sidebar.blog",
            "forms.newsletter.footer",
            "forms.search.autocomplete"
        ],
        "keywords": ["blog", "articles", "writing", "news"]
    },
    "landing_page": {
        "common_intents": [
            "navigation.header.with_cta",
            "landing.hero.gradient",
            "landing.features.icons",
            "content.testimonials.grid",
            "landing.cta.form",
            "forms.newsletter.modal"
        ],
        "keywords": ["landing", "landing page", "conversion"]
    },
    "restaurant": {
        "common_intents": [
            "navigation.header.minimal",
            "landing.hero.image",
            "content.gallery.grid",
            "forms.booking.calendar",
            "forms.contact.with_map"
        ],
        "keywords": ["restaurant", "cafe", "food", "dining", "menu"]
    },
    "fitness": {
        "common_intents": [
            "navigation.header.with_cta",
            "landing.hero.video",
            "content.team.grid",
            "pricing.table.simple",
            "forms.booking.time_slots"
        ],
        "keywords": ["fitness", "gym", "workout", "training", "health"]
    },
    "dashboard": {
        "common_intents": [
            "admin.dashboard.widgets",
            "navigation.sidebar.admin",
            "data.charts.dashboard",
            "data.table.sortable",
            "data.stats.cards"
        ],
        "keywords": ["dashboard", "admin", "panel", "analytics"]
    }
}

# ============================================================================
# FEATURE PATTERNS - For extracting specific features from prompts
# ============================================================================

FEATURE_PATTERNS = {
    "search": ["search", "search bar", "search box", "find"],
    "filter": ["filter", "filtering", "sort", "refine"],
    "pagination": ["pagination", "pages", "page numbers", "next/prev"],
    "social_login": ["google", "facebook", "social login", "oauth", "github"],
    "newsletter": ["newsletter", "subscribe", "email signup"],
    "mobile_menu": ["mobile menu", "hamburger", "responsive menu"],
    "sticky": ["sticky", "fixed", "pinned"],
    "dark_mode": ["dark mode", "theme toggle", "light/dark", "theme switcher"],
    "quantity_selector": ["quantity", "qty", "amount selector"],
    "wishlist": ["wishlist", "favorites", "save for later"],
    "reviews": ["reviews", "ratings", "stars"],
    "multi_step": ["multi-step", "wizard", "step by step", "steps"],
    "countdown": ["countdown", "timer", "limited time"],
    "video": ["video", "video background"],
    "animation": ["animated", "animation", "transitions"],
    "autocomplete": ["autocomplete", "suggestions", "auto-complete"],
    "lightbox": ["lightbox", "popup", "modal"],
    "carousel": ["carousel", "slider", "slideshow"],
    "map": ["map", "location", "google maps"],
    "calendar": ["calendar", "date picker"],
    "time_picker": ["time", "time picker", "time selection"],
    "drag_drop": ["drag", "drop", "drag and drop"],
    "infinite_scroll": ["infinite scroll", "lazy load"],
    "breadcrumbs": ["breadcrumbs", "navigation trail"],
    "tabs": ["tabs", "tabbed"],
    "accordion": ["accordion", "collapsible", "expandable"],
    "tooltip": ["tooltip", "hint", "help text"],
    "progress_bar": ["progress", "progress bar"],
    "file_upload": ["upload", "file upload", "attach"],
    "export": ["export", "download", "csv", "pdf"],
    "print": ["print", "print view"]
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_intent_path(domain: str, category: str, intent: str, variant: Optional[str] = None) -> str:
    """Generate intent path string"""
    path = f"{domain}.{category}.{intent}"
    if variant:
        path += f".{variant}"
    return path


def get_intent_info(domain: str, category: str, intent: str) -> Optional[Dict]:
    """Get intent information from taxonomy"""
    try:
        return INTENT_TAXONOMY[domain][category][intent]
    except KeyError:
        return None


def get_all_intents() -> List[str]:
    """Get list of all possible intent paths"""
    intents = []

    for domain, categories in INTENT_TAXONOMY.items():
        for category, intent_types in categories.items():
            for intent, info in intent_types.items():
                if intent in ['description', 'keywords', 'features']:
                    continue

                # Base intent
                intents.append(get_intent_path(domain, category, intent))

                # With variants
                if 'variants' in info:
                    for variant in info['variants'].keys():
                        intents.append(get_intent_path(domain, category, intent, variant))

    return intents


def get_website_type_intents(website_type: str) -> List[str]:
    """Get common intents for a website type"""
    if website_type in WEBSITE_TYPE_PATTERNS:
        return WEBSITE_TYPE_PATTERNS[website_type]['common_intents']
    return []


def detect_website_type(prompt: str) -> Optional[str]:
    """Detect website type from prompt"""
    prompt_lower = prompt.lower()

    for website_type, patterns in WEBSITE_TYPE_PATTERNS.items():
        keywords = patterns['keywords']
        if any(kw in prompt_lower for kw in keywords):
            return website_type

    return None
