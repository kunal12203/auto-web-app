"""
Generate comprehensive COMPONENT_CATALOG for all 202 template components
"""
from pathlib import Path
import json

COMPONENTS_DIR = Path("/home/user/auto-web-app/backend/templates/components")

# Define metadata for each category
CATEGORY_METADATA = {
    "alerts": {
        "type": "Alert",
        "base_keywords": ["alert", "notification", "message", "warning", "info", "error", "success"],
        "variants": {
            "AlertSuccess": {"desc": "Success alert with green styling and checkmark", "extra": ["success", "confirmation"]},
            "AlertError": {"desc": "Error alert with red styling and warning icon", "extra": ["error", "danger", "warning"]},
            "AlertInfo": {"desc": "Info alert with blue styling and information icon", "extra": ["info", "notice"]},
            "AlertWarning": {"desc": "Warning alert with yellow/orange styling", "extra": ["warning", "caution"]},
            "AlertDismissible": {"desc": "Dismissible alert with close button", "extra": ["closeable", "dismiss"]},
            "AlertWithAction": {"desc": "Alert with action button", "extra": ["action", "cta"]}
        }
    },
    "blogs": {
        "type": "Blog",
        "base_keywords": ["blog", "article", "post", "news", "content", "writing"],
        "variants": {
            "BlogGrid": {"desc": "Grid layout of blog posts with images and excerpts", "extra": ["grid", "cards"]},
            "BlogList": {"desc": "Vertical list of blog posts with metadata", "extra": ["list", "vertical"]},
            "BlogFeatured": {"desc": "Featured blog post with large image and detailed preview", "extra": ["featured", "highlight"]},
            "BlogMinimal": {"desc": "Minimal blog list with clean typography", "extra": ["minimal", "simple"]},
            "BlogMasonry": {"desc": "Masonry-style blog grid with varied heights", "extra": ["masonry", "pinterest"]},
            "BlogTimeline": {"desc": "Timeline-based blog layout with chronological ordering", "extra": ["timeline", "chronological"]},
            "BlogSidebar": {"desc": "Blog layout with sidebar for categories and tags", "extra": ["sidebar", "categories"]}
        }
    },
    "cards": {
        "type": "Card",
        "base_keywords": ["card", "content", "info", "preview"],
        "variants": {
            "CardBasic": {"desc": "Basic card with title, description, and image", "extra": ["basic", "simple"]},
            "CardWithButton": {"desc": "Card with call-to-action button", "extra": ["cta", "button"]},
            "CardHover": {"desc": "Card with hover effects and animations", "extra": ["hover", "interactive"]},
            "CardImage": {"desc": "Image-focused card with minimal text", "extra": ["image", "photo"]},
            "CardPricing": {"desc": "Pricing card with features list", "extra": ["pricing", "plan"]},
            "CardProfile": {"desc": "Profile card for team members or users", "extra": ["profile", "team", "person"]},
            "CardBlog": {"desc": "Blog post card with excerpt and metadata", "extra": ["blog", "article"]},
            "CardProduct": {"desc": "Product card for e-commerce", "extra": ["product", "shop", "ecommerce"]},
            "CardTestimonial": {"desc": "Testimonial card with quote and author", "extra": ["testimonial", "review"]},
            "CardStats": {"desc": "Statistics card with number and label", "extra": ["stats", "metrics", "numbers"]}
        }
    },
    "contacts": {
        "type": "Contact",
        "base_keywords": ["contact", "form", "get in touch", "reach us", "email"],
        "variants": {
            "ContactForm": {"desc": "Contact form with name, email, and message fields", "extra": ["form", "submit"]},
            "ContactInfo": {"desc": "Contact information display with address, phone, email", "extra": ["info", "details"]},
            "ContactMap": {"desc": "Contact section with integrated map", "extra": ["map", "location"]},
            "ContactMinimal": {"desc": "Minimal contact form with essential fields only", "extra": ["minimal", "simple"]},
            "ContactSplit": {"desc": "Split layout with form and contact info side-by-side", "extra": ["split", "two-column"]},
            "ContactWithSocial": {"desc": "Contact section with social media links", "extra": ["social", "links"]},
            "ContactCard": {"desc": "Card-based contact layout", "extra": ["card", "boxed"]},
            "ContactInline": {"desc": "Inline contact form for embedding", "extra": ["inline", "embedded"]}
        }
    },
    "ctas": {
        "type": "CTA",
        "base_keywords": ["cta", "call to action", "signup", "get started", "button"],
        "variants": {
            "CTASimple": {"desc": "Simple CTA with headline and button", "extra": ["simple", "basic"]},
            "CTABanner": {"desc": "Full-width banner CTA with prominent styling", "extra": ["banner", "full-width"]},
            "CTAWithImage": {"desc": "CTA section with supporting image or icon", "extra": ["image", "visual"]},
            "CTAMinimal": {"desc": "Minimal CTA with clean design", "extra": ["minimal", "clean"]},
            "CTABoxed": {"desc": "Boxed CTA with border and background", "extra": ["boxed", "container"]},
            "CTASplit": {"desc": "Split CTA with multiple actions or options", "extra": ["split", "multiple"]},
            "CTANewsletter": {"desc": "Newsletter signup CTA with email input", "extra": ["newsletter", "email", "subscribe"]},
            "CTAVideo": {"desc": "Video-based CTA with play button", "extra": ["video", "media"]}
        }
    },
    "ecommerce": {
        "type": "Ecommerce",
        "base_keywords": ["ecommerce", "shop", "store", "product", "buy", "cart"],
        "variants": {
            "ProductGrid": {"desc": "Grid of products with images, prices, and add to cart", "extra": ["grid", "catalog"]},
            "ProductList": {"desc": "List view of products with detailed information", "extra": ["list", "detailed"]},
            "ProductCard": {"desc": "Individual product card component", "extra": ["card", "item"]},
            "ProductFeatured": {"desc": "Featured product showcase with large display", "extra": ["featured", "highlight"]},
            "ShoppingCart": {"desc": "Shopping cart with items, quantities, and totals", "extra": ["cart", "checkout"]},
            "Checkout": {"desc": "Checkout form with billing and shipping", "extra": ["checkout", "payment"]},
            "ProductFilters": {"desc": "Product filtering and sorting interface", "extra": ["filter", "sort", "search"]},
            "ProductQuickView": {"desc": "Quick view modal for products", "extra": ["quickview", "modal"]},
            "WishlistButton": {"desc": "Add to wishlist button component", "extra": ["wishlist", "favorite"]},
            "ProductReviews": {"desc": "Product reviews and ratings section", "extra": ["reviews", "ratings"]},
            "RelatedProducts": {"desc": "Related products carousel", "extra": ["related", "suggestions"]},
            "ProductComparison": {"desc": "Product comparison table", "extra": ["compare", "comparison"]}
        }
    },
    "faqs": {
        "type": "FAQ",
        "base_keywords": ["faq", "questions", "answers", "help", "support"],
        "variants": {
            "FAQAccordion": {"desc": "FAQ section with accordion-style expandable items", "extra": ["accordion", "collapsible"]},
            "FAQGrid": {"desc": "Grid layout of frequently asked questions", "extra": ["grid", "cards"]},
            "FAQMinimal": {"desc": "Minimal FAQ list with simple styling", "extra": ["minimal", "simple"]},
            "FAQWithCategories": {"desc": "FAQ organized by categories or topics", "extra": ["categories", "topics"]},
            "FAQSearchable": {"desc": "Searchable FAQ with filter functionality", "extra": ["search", "filter"]}
        }
    },
    "features": {
        "type": "Features",
        "base_keywords": ["features", "services", "benefits", "offerings", "what we do"],
        "variants": {
            "FeaturesGrid": {"desc": "Grid layout of features with icons and descriptions", "extra": ["grid", "cards"]},
            "FeaturesList": {"desc": "Vertical list of features with detailed descriptions", "extra": ["list", "vertical"]},
            "FeaturesWithIcons": {"desc": "Features highlighted with custom icons", "extra": ["icons", "visual"]},
            "FeaturesAlternating": {"desc": "Alternating layout with images and text", "extra": ["alternating", "image"]},
            "FeaturesCompact": {"desc": "Compact features layout for quick scanning", "extra": ["compact", "dense"]}
        }
    },
    "footers": {
        "type": "Footer",
        "base_keywords": ["footer", "bottom", "links", "copyright", "social"],
        "variants": {
            "FooterComprehensive": {"desc": "Full footer with multiple columns, links, and social media", "extra": ["comprehensive", "full", "detailed"]},
            "FooterMinimal": {"desc": "Minimal footer with brand name and basic links", "extra": ["minimal", "simple", "clean"]},
            "FooterNewsletter": {"desc": "Footer with newsletter signup", "extra": ["newsletter", "subscribe"]},
            "FooterCentered": {"desc": "Centered footer layout", "extra": ["centered", "symmetric"]},
            "FooterSocial": {"desc": "Footer emphasizing social media links", "extra": ["social", "icons"]},
            "FooterApp": {"desc": "Footer for app pages with app store links", "extra": ["app", "download"]},
            "FooterMultiColumn": {"desc": "Multi-column footer with organized link sections", "extra": ["columns", "organized"]},
            "FooterSimple": {"desc": "Simple single-line footer", "extra": ["simple", "compact"]}
        }
    },
    "forms": {
        "type": "Form",
        "base_keywords": ["form", "input", "submit", "fields"],
        "variants": {
            "FormContact": {"desc": "Contact form with name, email, message", "extra": ["contact", "message"]},
            "FormNewsletter": {"desc": "Newsletter subscription form", "extra": ["newsletter", "subscribe", "email"]},
            "FormLogin": {"desc": "Login form with email and password", "extra": ["login", "signin", "auth"]},
            "FormSignup": {"desc": "Signup/registration form", "extra": ["signup", "register", "create account"]},
            "FormBooking": {"desc": "Booking/appointment form with date and time", "extra": ["booking", "appointment", "reservation"]},
            "FormSearch": {"desc": "Search form with filters", "extra": ["search", "filter", "find"]},
            "FormMultistep": {"desc": "Multi-step form with progress indicator", "extra": ["multistep", "wizard", "progress"]},
            "FormInline": {"desc": "Inline form layout", "extra": ["inline", "compact"]}
        }
    },
    "galleries": {
        "type": "Gallery",
        "base_keywords": ["gallery", "images", "photos", "portfolio", "showcase"],
        "variants": {
            "GalleryGrid": {"desc": "Grid-based image gallery", "extra": ["grid", "uniform"]},
            "GalleryMasonry": {"desc": "Masonry-style gallery with varied image sizes", "extra": ["masonry", "pinterest"]},
            "GalleryLightbox": {"desc": "Gallery with lightbox/modal image viewer", "extra": ["lightbox", "modal", "popup"]},
            "GalleryCarousel": {"desc": "Carousel/slider image gallery", "extra": ["carousel", "slider"]},
            "GalleryMinimal": {"desc": "Minimal gallery with clean layout", "extra": ["minimal", "simple"]},
            "GalleryWithCaptions": {"desc": "Gallery with image captions and descriptions", "extra": ["captions", "descriptions"]},
            "GalleryFullscreen": {"desc": "Fullscreen gallery experience", "extra": ["fullscreen", "immersive"]},
            "GalleryThumbnails": {"desc": "Gallery with thumbnail navigation", "extra": ["thumbnails", "preview"]}
        }
    },
    "headers": {
        "type": "Header",
        "base_keywords": ["header", "navigation", "nav", "menu", "top"],
        "variants": {
            "HeaderWithCTA": {"desc": "Header with navigation and call-to-action button", "extra": ["cta", "button"]},
            "HeaderMinimal": {"desc": "Minimal header with logo and basic navigation", "extra": ["minimal", "simple"]},
            "HeaderTransparent": {"desc": "Transparent header for hero overlays", "extra": ["transparent", "overlay"]},
            "HeaderSticky": {"desc": "Sticky header that stays at top when scrolling", "extra": ["sticky", "fixed"]},
            "HeaderMega": {"desc": "Header with mega menu dropdown", "extra": ["mega", "dropdown"]},
            "HeaderWithSearch": {"desc": "Header with integrated search bar", "extra": ["search", "find"]},
            "HeaderCentered": {"desc": "Centered header layout", "extra": ["centered", "symmetric"]},
            "HeaderSplit": {"desc": "Split header with logo and navigation separated", "extra": ["split", "divided"]}
        }
    },
    "heroes": {
        "type": "Hero",
        "base_keywords": ["hero", "banner", "landing", "headline", "main"],
        "variants": {
            "HeroImage": {"desc": "Hero section with headline, CTA, and image", "extra": ["image", "visual"]},
            "HeroCentered": {"desc": "Centered hero with headline and call-to-action", "extra": ["centered", "symmetric"]},
            "HeroMinimal": {"desc": "Minimal hero with essential elements only", "extra": ["minimal", "simple"]},
            "HeroVideo": {"desc": "Hero with background video", "extra": ["video", "media"]},
            "HeroSplit": {"desc": "Split hero with content and image side-by-side", "extra": ["split", "two-column"]},
            "HeroFullscreen": {"desc": "Fullscreen hero covering viewport", "extra": ["fullscreen", "viewport"]},
            "HeroWithForm": {"desc": "Hero section with embedded form", "extra": ["form", "signup"]},
            "HeroGradient": {"desc": "Hero with gradient background", "extra": ["gradient", "color"]},
            "HeroAnimated": {"desc": "Hero with animated elements", "extra": ["animated", "motion"]},
            "HeroMultiCTA": {"desc": "Hero with multiple call-to-action buttons", "extra": ["multiple", "actions"]}
        }
    },
    "logos": {
        "type": "LogoGrid",
        "base_keywords": ["logo", "brands", "partners", "clients", "companies"],
        "variants": {
            "LogoGridSimple": {"desc": "Simple grid of partner/client logos", "extra": ["grid", "simple"]},
            "LogoGridAnimated": {"desc": "Animated logo grid with hover effects", "extra": ["animated", "interactive"]},
            "LogoCarousel": {"desc": "Scrolling carousel of logos", "extra": ["carousel", "slider"]}
        }
    },
    "misc": {
        "type": "Utility",
        "base_keywords": ["utility", "helper", "component"],
        "variants": {
            "Breadcrumbs": {"desc": "Breadcrumb navigation component", "extra": ["breadcrumb", "navigation", "path"]},
            "Divider": {"desc": "Visual divider/separator component", "extra": ["divider", "separator", "line"]},
            "Badge": {"desc": "Badge component for labels and tags", "extra": ["badge", "label", "tag"]},
            "Tooltip": {"desc": "Tooltip component for additional information", "extra": ["tooltip", "hint", "info"]},
            "Avatar": {"desc": "User avatar component", "extra": ["avatar", "profile", "user"]},
            "Spinner": {"desc": "Loading spinner component", "extra": ["spinner", "loading", "loader"]},
            "Skeleton": {"desc": "Skeleton loading placeholder", "extra": ["skeleton", "placeholder", "loading"]},
            "BackToTop": {"desc": "Back to top button", "extra": ["scroll", "top", "up"]},
            "ShareButtons": {"desc": "Social share buttons", "extra": ["share", "social", "media"]},
            "CookieConsent": {"desc": "Cookie consent banner", "extra": ["cookie", "gdpr", "consent"]},
            "LanguageSwitcher": {"desc": "Language/locale switcher", "extra": ["language", "locale", "i18n"]},
            "ThemeToggle": {"desc": "Dark/light theme toggle", "extra": ["theme", "dark", "light"]},
            "Pagination": {"desc": "Pagination component for content", "extra": ["pagination", "pages", "navigation"]},
            "CountdownTimer": {"desc": "Countdown timer component", "extra": ["countdown", "timer", "deadline"]},
            "ReadingTime": {"desc": "Reading time estimate display", "extra": ["reading", "time", "estimate"]},
            "QRCode": {"desc": "QR code display component", "extra": ["qr", "code", "scan"]},
            "PrintButton": {"desc": "Print page button", "extra": ["print", "pdf"]},
            "EmailSignature": {"desc": "Email signature component", "extra": ["email", "signature", "contact"]},
            "SkipToContent": {"desc": "Accessibility skip to content link", "extra": ["accessibility", "a11y", "skip"]},
            "LiveChat": {"desc": "Live chat widget placeholder", "extra": ["chat", "support", "help"]}
        }
    },
    "modals": {
        "type": "Modal",
        "base_keywords": ["modal", "popup", "dialog", "overlay"],
        "variants": {
            "ModalBasic": {"desc": "Basic modal dialog with header and content", "extra": ["basic", "simple"]},
            "ModalConfirm": {"desc": "Confirmation modal with yes/no actions", "extra": ["confirm", "prompt"]},
            "ModalForm": {"desc": "Modal with embedded form", "extra": ["form", "input"]}
        }
    },
    "navigation": {
        "type": "Navigation",
        "base_keywords": ["navigation", "nav", "menu", "links"],
        "variants": {
            "NavHorizontal": {"desc": "Horizontal navigation bar", "extra": ["horizontal", "bar"]},
            "NavVertical": {"desc": "Vertical sidebar navigation", "extra": ["vertical", "sidebar"]},
            "NavDropdown": {"desc": "Navigation with dropdown menus", "extra": ["dropdown", "submenu"]},
            "NavMobile": {"desc": "Mobile-responsive hamburger navigation", "extra": ["mobile", "hamburger"]},
            "NavTabs": {"desc": "Tab-style navigation", "extra": ["tabs", "tabbed"]},
            "NavBreadcrumb": {"desc": "Breadcrumb navigation trail", "extra": ["breadcrumb", "trail"]}
        }
    },
    "newsletters": {
        "type": "Newsletter",
        "base_keywords": ["newsletter", "subscribe", "email", "signup"],
        "variants": {
            "NewsletterSimple": {"desc": "Simple newsletter signup with email input", "extra": ["simple", "basic"]},
            "NewsletterBanner": {"desc": "Full-width newsletter banner", "extra": ["banner", "prominent"]},
            "NewsletterPopup": {"desc": "Newsletter popup/modal", "extra": ["popup", "modal"]},
            "NewsletterInline": {"desc": "Inline newsletter form for embedding", "extra": ["inline", "embedded"]},
            "NewsletterWithBenefits": {"desc": "Newsletter signup highlighting benefits", "extra": ["benefits", "features"]},
            "NewsletterMinimal": {"desc": "Minimal newsletter signup", "extra": ["minimal", "clean"]},
            "NewsletterFooter": {"desc": "Newsletter signup for footer placement", "extra": ["footer", "bottom"]}
        }
    },
    "pricing": {
        "type": "Pricing",
        "base_keywords": ["pricing", "plans", "subscription", "tiers", "cost"],
        "variants": {
            "PricingCards": {"desc": "Pricing table with multiple plan tiers", "extra": ["cards", "tiers"]},
            "PricingTable": {"desc": "Detailed pricing comparison table", "extra": ["table", "comparison"]},
            "PricingToggle": {"desc": "Pricing with monthly/yearly toggle", "extra": ["toggle", "switch"]},
            "PricingMinimal": {"desc": "Minimal pricing display", "extra": ["minimal", "simple"]}
        }
    },
    "progress": {
        "type": "Progress",
        "base_keywords": ["progress", "loading", "steps", "status"],
        "variants": {
            "ProgressBar": {"desc": "Linear progress bar", "extra": ["bar", "linear"]},
            "ProgressCircular": {"desc": "Circular progress indicator", "extra": ["circular", "radial"]},
            "ProgressSteps": {"desc": "Multi-step progress indicator", "extra": ["steps", "stepper"]},
            "ProgressTimeline": {"desc": "Timeline-based progress", "extra": ["timeline", "chronological"]}
        }
    },
    "restaurant": {
        "type": "Restaurant",
        "base_keywords": ["restaurant", "menu", "food", "dining", "cafe"],
        "variants": {
            "MenuGrid": {"desc": "Grid layout of menu items with images and prices", "extra": ["menu", "grid", "items"]},
            "MenuList": {"desc": "List-style menu with categories", "extra": ["menu", "list", "categories"]},
            "MenuCategories": {"desc": "Menu organized by food categories", "extra": ["categories", "sections"]},
            "ReservationForm": {"desc": "Table reservation form", "extra": ["reservation", "booking", "table"]},
            "HoursLocation": {"desc": "Restaurant hours and location info", "extra": ["hours", "location", "address"]},
            "ChefProfile": {"desc": "Chef profile section", "extra": ["chef", "team", "about"]},
            "SpecialsCarousel": {"desc": "Daily specials carousel", "extra": ["specials", "featured", "carousel"]},
            "CateringInfo": {"desc": "Catering services information", "extra": ["catering", "events", "services"]},
            "DeliveryOptions": {"desc": "Delivery and pickup options", "extra": ["delivery", "pickup", "order"]},
            "DiningExperience": {"desc": "Dining experience showcase with images", "extra": ["experience", "ambiance", "photos"]}
        }
    },
    "saas": {
        "type": "SaaS",
        "base_keywords": ["saas", "software", "platform", "app", "tool"],
        "variants": {
            "FeatureShowcase": {"desc": "SaaS feature showcase with screenshots", "extra": ["features", "showcase", "demo"]},
            "IntegrationGrid": {"desc": "Grid of integrations and partnerships", "extra": ["integrations", "partners"]},
            "DashboardPreview": {"desc": "Dashboard screenshot preview", "extra": ["dashboard", "preview", "ui"]},
            "APIDocumentation": {"desc": "API documentation section", "extra": ["api", "docs", "developers"]},
            "UseCases": {"desc": "Use cases and customer stories", "extra": ["use cases", "examples", "stories"]},
            "SecurityBadges": {"desc": "Security and compliance badges", "extra": ["security", "compliance", "trust"]},
            "PricingComparison": {"desc": "Detailed pricing plan comparison", "extra": ["pricing", "plans", "comparison"]},
            "FreeTrial": {"desc": "Free trial signup CTA", "extra": ["trial", "signup", "cta"]},
            "StatusPage": {"desc": "Service status and uptime display", "extra": ["status", "uptime", "health"]},
            "ChangelogPreview": {"desc": "Product changelog/updates preview", "extra": ["changelog", "updates", "releases"]}
        }
    },
    "search": {
        "type": "Search",
        "base_keywords": ["search", "find", "filter", "query"],
        "variants": {
            "SearchBar": {"desc": "Search bar with autocomplete", "extra": ["bar", "autocomplete"]},
            "SearchWithFilters": {"desc": "Search with advanced filters", "extra": ["filters", "advanced"]},
            "SearchResults": {"desc": "Search results display", "extra": ["results", "listing"]}
        }
    },
    "social": {
        "type": "Social",
        "base_keywords": ["social", "media", "share", "follow"],
        "variants": {
            "SocialLinks": {"desc": "Social media links with icons", "extra": ["links", "icons"]},
            "SocialShare": {"desc": "Social share buttons", "extra": ["share", "buttons"]},
            "SocialFeed": {"desc": "Social media feed embed", "extra": ["feed", "embed", "timeline"]}
        }
    },
    "stats": {
        "type": "Stats",
        "base_keywords": ["stats", "statistics", "numbers", "metrics", "achievements"],
        "variants": {
            "StatsGrid": {"desc": "Grid of statistics with numbers and labels", "extra": ["grid", "cards"]},
            "StatsHorizontal": {"desc": "Horizontal row of statistics", "extra": ["horizontal", "row"]},
            "StatsAnimated": {"desc": "Animated counting statistics", "extra": ["animated", "counter"]},
            "StatsWithIcons": {"desc": "Statistics with icon graphics", "extra": ["icons", "visual"]},
            "StatsMinimal": {"desc": "Minimal statistics display", "extra": ["minimal", "clean"]}
        }
    },
    "tabs": {
        "type": "Tabs",
        "base_keywords": ["tabs", "tabbed", "panels", "sections"],
        "variants": {
            "TabsBasic": {"desc": "Basic tabbed interface", "extra": ["basic", "simple"]},
            "TabsVertical": {"desc": "Vertical tabs layout", "extra": ["vertical", "sidebar"]},
            "TabsAccordion": {"desc": "Accordion-style tabs for mobile", "extra": ["accordion", "mobile"]}
        }
    },
    "teams": {
        "type": "Team",
        "base_keywords": ["team", "staff", "members", "people", "about us"],
        "variants": {
            "TeamGrid": {"desc": "Grid of team members with photos and bios", "extra": ["grid", "cards"]},
            "TeamList": {"desc": "List view of team members", "extra": ["list", "vertical"]},
            "TeamMinimal": {"desc": "Minimal team display", "extra": ["minimal", "simple"]},
            "TeamWithSocial": {"desc": "Team members with social links", "extra": ["social", "links"]}
        }
    },
    "testimonials": {
        "type": "Testimonials",
        "base_keywords": ["testimonials", "reviews", "feedback", "customers", "quotes"],
        "variants": {
            "TestimonialsGrid": {"desc": "Grid of customer testimonials", "extra": ["grid", "cards"]},
            "TestimonialsCarousel": {"desc": "Carousel of testimonials", "extra": ["carousel", "slider"]},
            "TestimonialsMinimal": {"desc": "Minimal testimonials display", "extra": ["minimal", "simple"]},
            "TestimonialsWithRatings": {"desc": "Testimonials with star ratings", "extra": ["ratings", "stars", "reviews"]}
        }
    },
    "timelines": {
        "type": "Timeline",
        "base_keywords": ["timeline", "history", "chronological", "roadmap", "milestones"],
        "variants": {
            "TimelineVertical": {"desc": "Vertical timeline with dates and events", "extra": ["vertical", "chronological"]},
            "TimelineHorizontal": {"desc": "Horizontal timeline", "extra": ["horizontal", "linear"]},
            "TimelineRoadmap": {"desc": "Product roadmap timeline", "extra": ["roadmap", "future", "plans"]},
            "TimelineHistory": {"desc": "Company history timeline", "extra": ["history", "about", "story"]},
            "TimelineMilestones": {"desc": "Milestones and achievements timeline", "extra": ["milestones", "achievements"]}
        }
    },
    "videos": {
        "type": "Video",
        "base_keywords": ["video", "media", "youtube", "vimeo", "player"],
        "variants": {
            "VideoHero": {"desc": "Video background hero section", "extra": ["hero", "background"]},
            "VideoEmbed": {"desc": "Embedded video player", "extra": ["embed", "player"]},
            "VideoGrid": {"desc": "Grid of video thumbnails", "extra": ["grid", "gallery"]},
            "VideoModal": {"desc": "Video player in modal/lightbox", "extra": ["modal", "lightbox", "popup"]},
            "VideoTestimonial": {"desc": "Video testimonial player", "extra": ["testimonial", "review"]}
        }
    }
}

def generate_catalog():
    """Generate the complete COMPONENT_CATALOG dictionary"""
    catalog = {}

    # Scan all component directories
    for category_dir in sorted(COMPONENTS_DIR.iterdir()):
        if not category_dir.is_dir():
            continue

        category_name = category_dir.name

        if category_name not in CATEGORY_METADATA:
            print(f"Warning: No metadata for category '{category_name}'")
            continue

        metadata = CATEGORY_METADATA[category_name]

        # Get all .jsx files in this category
        for component_file in sorted(category_dir.glob("*.jsx")):
            component_name = component_file.stem
            template_path = f"{category_name}/{component_name}"

            # Get variant-specific metadata
            variant_meta = metadata["variants"].get(component_name, {
                "desc": f"{metadata['type']} component",
                "extra": []
            })

            # Build keywords list
            keywords = metadata["base_keywords"] + variant_meta["extra"]

            # Create catalog entry
            catalog[template_path] = {
                "description": variant_meta["desc"],
                "keywords": keywords,
                "type": metadata["type"]
            }

    return catalog

def format_catalog_as_python(catalog):
    """Format the catalog as Python code"""
    lines = ["COMPONENT_CATALOG = {"]

    for path, info in sorted(catalog.items()):
        lines.append(f'    "{path}": {{')
        lines.append(f'        "description": "{info["description"]}",')

        # Format keywords nicely
        keywords_str = ', '.join(f'"{k}"' for k in info["keywords"])
        lines.append(f'        "keywords": [{keywords_str}],')
        lines.append(f'        "type": "{info["type"]}"')
        lines.append('    },')

    lines.append("}")

    return "\n".join(lines)

if __name__ == "__main__":
    print("Generating COMPONENT_CATALOG for all 202 components...")

    catalog = generate_catalog()

    print(f"\nGenerated catalog with {len(catalog)} components")
    print(f"\nWriting to component_catalog_generated.py...")

    # Write to file
    catalog_code = format_catalog_as_python(catalog)

    with open("/home/user/auto-web-app/backend/component_catalog_generated.py", "w") as f:
        f.write('"""\n')
        f.write('Auto-generated COMPONENT_CATALOG for all 202 template components\n')
        f.write('Generated by generate_component_catalog.py\n')
        f.write('"""\n\n')
        f.write(catalog_code)

    print("Done! Catalog written to component_catalog_generated.py")
    print(f"\nSample entries:")
    for i, (path, info) in enumerate(list(catalog.items())[:5]):
        print(f'\n  "{path}":')
        print(f'    Description: {info["description"]}')
        print(f'    Keywords: {", ".join(info["keywords"][:5])}...')
