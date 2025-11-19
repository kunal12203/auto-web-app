"""
Navigation Template Generator - Generates headers, footers, sidebars, menus
Target: 1,000 navigation templates
"""

import logging
from typing import List
from template_generator_core import (
    BaseTemplateGenerator,
    TemplateSpec,
    VariationConfig,
    sanitize_component_name,
    generate_component_imports
)

logger = logging.getLogger(__name__)


# ============================================================================
# HEADER/NAVIGATION GENERATOR
# ============================================================================

class HeaderGenerator(BaseTemplateGenerator):
    """
    Generates header and navigation templates

    Variations:
    - Simple headers (100)
    - Headers with CTA (150)
    - Headers with mega menu (100)
    - Transparent headers (80)
    - Sticky headers (80)
    - Mobile-first headers (90)
    """

    def get_domain(self) -> str:
        return "navigation"

    def get_category(self) -> str:
        return "header"

    def get_variation_config(self) -> VariationConfig:
        """Define header variations"""
        return VariationConfig(
            styles=[
                'modern',
                'minimal',
                'gradient',
                'glassmorphism',
                'professional',
                'creative',
                'corporate',
                'startup'
            ],
            layouts=[
                'horizontal',
                'centered_logo',
                'split',
                'transparent',
                'boxed',
                'fullwidth'
            ],
            features=[
                # Basic navigation
                ['logo', 'nav_links'],
                ['logo', 'nav_links', 'mobile_menu'],

                # With CTA
                ['logo', 'nav_links', 'cta_button'],
                ['logo', 'nav_links', 'cta_button', 'mobile_menu'],
                ['logo', 'nav_links', 'cta_button', 'secondary_cta'],

                # With search
                ['logo', 'nav_links', 'search_bar'],
                ['logo', 'nav_links', 'search_bar', 'cta_button'],

                # With dropdown
                ['logo', 'nav_links', 'dropdown_menu'],
                ['logo', 'nav_links', 'dropdown_menu', 'cta_button'],
                ['logo', 'nav_links', 'mega_menu'],

                # With user menu
                ['logo', 'nav_links', 'user_menu'],
                ['logo', 'nav_links', 'user_menu', 'notifications'],
                ['logo', 'nav_links', 'user_menu', 'notifications', 'cart'],

                # Sticky/Fixed
                ['logo', 'nav_links', 'sticky'],
                ['logo', 'nav_links', 'sticky', 'scroll_effect'],

                # Language/Theme switcher
                ['logo', 'nav_links', 'language_switcher'],
                ['logo', 'nav_links', 'theme_toggle'],
                ['logo', 'nav_links', 'theme_toggle', 'language_switcher'],
            ],
            animations=[
                'none',
                'fade',
                'slide_down',
                'reveal'
            ],
            complexities=[
                'simple',
                'standard',
                'advanced'
            ]
        )

    def generate_code(self, spec: TemplateSpec) -> str:
        """Generate React header component"""
        component_name = spec.get_name()

        # Generate imports
        imports = generate_component_imports(spec.features)
        imports += "\nimport { FiMenu, FiX, FiSearch, FiUser, FiBell, FiShoppingCart, FiChevronDown } from 'react-icons/fi'"

        # Build state declarations
        state_declarations = [
            "const [isMenuOpen, setIsMenuOpen] = React.useState(false);"
        ]

        if 'scroll_effect' in spec.features:
            state_declarations.append("const [isScrolled, setIsScrolled] = React.useState(false);")

        if 'user_menu' in spec.features:
            state_declarations.append("const [isUserMenuOpen, setIsUserMenuOpen] = React.useState(false);")

        if 'search_bar' in spec.features:
            state_declarations.append("const [searchQuery, setSearchQuery] = React.useState('');")

        states_code = '\n  '.join(state_declarations)

        # Build scroll effect
        scroll_effect_code = self._generate_scroll_effect(spec) if 'scroll_effect' in spec.features else ''

        # Build class names
        sticky_class = ' sticky' if 'sticky' in spec.features else ''
        scrolled_class = ' scrolled' if 'scroll_effect' in spec.features else ''
        class_names = f"{spec.layout}-layout {spec.style}-style {component_name.lower()}{sticky_class}{scrolled_class}"

        code = f'''{imports}

/**
 * {component_name} Component
 *
 * {spec.style.title()} style navigation header
 * Layout: {spec.layout}
 * Features: {', '.join(spec.features)}
 *
 * @component
 */
const {component_name} = () => {{
  {states_code}

  {scroll_effect_code}

  const toggleMenu = () => setIsMenuOpen(!isMenuOpen);

  return (
    <header className="{class_names}">
      <div className="header-container">
'''

        # Generate layout based on type
        if spec.layout == 'centered_logo':
            code += self._generate_centered_logo_layout(spec)
        elif spec.layout == 'split':
            code += self._generate_split_layout(spec)
        else:
            code += self._generate_standard_layout(spec)

        code += '''      </div>

      {/* Mobile Menu */}
      {isMenuOpen && (
        <div className="mobile-menu">
          <nav className="mobile-nav">
            {/* Navigation items */}
          </nav>
        </div>
      )}
    </header>
  );
};

export default {component_name};
'''.format(component_name=component_name)

        return code

    def _generate_standard_layout(self, spec: TemplateSpec) -> str:
        """Standard horizontal header layout"""
        return f'''        <div className="header-left">
          {self._generate_logo()}
          {self._generate_nav_links(spec)}
        </div>

        <div className="header-right">
          {self._generate_search_bar(spec) if 'search_bar' in spec.features else ''}
          {self._generate_theme_toggle(spec) if 'theme_toggle' in spec.features else ''}
          {self._generate_language_switcher(spec) if 'language_switcher' in spec.features else ''}
          {self._generate_user_menu(spec) if 'user_menu' in spec.features else ''}
          {self._generate_notifications(spec) if 'notifications' in spec.features else ''}
          {self._generate_cart(spec) if 'cart' in spec.features else ''}
          {self._generate_cta_buttons(spec)}
          {self._generate_mobile_toggle() if 'mobile_menu' in spec.features else ''}
        </div>'''

    def _generate_centered_logo_layout(self, spec: TemplateSpec) -> str:
        """Centered logo layout"""
        return f'''        <div className="header-top">
          <div className="left-nav">
            {self._generate_nav_links(spec, side='left')}
          </div>

          {self._generate_logo()}

          <div className="right-nav">
            {self._generate_nav_links(spec, side='right')}
            {self._generate_cta_buttons(spec)}
          </div>
        </div>'''

    def _generate_split_layout(self, spec: TemplateSpec) -> str:
        """Split layout with logo on left, everything else on right"""
        return f'''        {self._generate_logo()}

        <div className="header-content">
          {self._generate_nav_links(spec)}
          <div className="header-actions">
            {self._generate_search_bar(spec) if 'search_bar' in spec.features else ''}
            {self._generate_cta_buttons(spec)}
          </div>
        </div>

        {self._generate_mobile_toggle() if 'mobile_menu' in spec.features else ''}'''

    def _generate_logo(self) -> str:
        """Generate logo component"""
        return '''<div className="logo">
            <a href="/">
              <img src="/logo.svg" alt="Logo" />
            </a>
          </div>'''

    def _generate_nav_links(self, spec: TemplateSpec, side: str = 'all') -> str:
        """Generate navigation links"""
        has_dropdown = 'dropdown_menu' in spec.features
        has_mega = 'mega_menu' in spec.features

        dropdown_html = '''
                  <FiChevronDown />
                  <div className="dropdown-menu">
                    <a href="/product/feature-1">Feature 1</a>
                    <a href="/product/feature-2">Feature 2</a>
                    <a href="/product/feature-3">Feature 3</a>
                  </div>''' if has_dropdown else ''

        mega_menu_html = '''
                  <FiChevronDown />
                  <div className="mega-menu">
                    <div className="mega-menu-section">
                      <h4>Products</h4>
                      <a href="#">Product 1</a>
                      <a href="#">Product 2</a>
                    </div>
                    <div className="mega-menu-section">
                      <h4>Solutions</h4>
                      <a href="#">Solution 1</a>
                      <a href="#">Solution 2</a>
                    </div>
                  </div>''' if has_mega else ''

        return f'''<nav className="main-nav">
            <a href="/">Home</a>
            <a href="/about">About</a>
            <div className="nav-item-dropdown">
              <a href="/products">Products{dropdown_html if has_dropdown else ''}{mega_menu_html if has_mega else ''}</a>
            </div>
            <a href="/pricing">Pricing</a>
            <a href="/contact">Contact</a>
          </nav>'''

    def _generate_search_bar(self, spec: TemplateSpec) -> str:
        """Generate search bar"""
        return '''<div className="search-bar">
            <FiSearch />
            <input
              type="text"
              placeholder="Search..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </div>'''

    def _generate_theme_toggle(self, spec: TemplateSpec) -> str:
        """Generate theme toggle button"""
        return '''<button className="theme-toggle" onClick={() => {}}>
            🌙
          </button>'''

    def _generate_language_switcher(self, spec: TemplateSpec) -> str:
        """Generate language switcher"""
        return '''<select className="language-switcher">
            <option value="en">EN</option>
            <option value="es">ES</option>
            <option value="fr">FR</option>
          </select>'''

    def _generate_user_menu(self, spec: TemplateSpec) -> str:
        """Generate user menu dropdown"""
        return '''<div className="user-menu">
            <button onClick={() => setIsUserMenuOpen(!isUserMenuOpen)}>
              <FiUser />
            </button>
            {isUserMenuOpen && (
              <div className="user-dropdown">
                <a href="/profile">Profile</a>
                <a href="/settings">Settings</a>
                <a href="/logout">Logout</a>
              </div>
            )}
          </div>'''

    def _generate_notifications(self, spec: TemplateSpec) -> str:
        """Generate notifications icon"""
        return '''<button className="notifications-btn">
            <FiBell />
            <span className="badge">3</span>
          </button>'''

    def _generate_cart(self, spec: TemplateSpec) -> str:
        """Generate shopping cart icon"""
        return '''<button className="cart-btn">
            <FiShoppingCart />
            <span className="badge">2</span>
          </button>'''

    def _generate_cta_buttons(self, spec: TemplateSpec) -> str:
        """Generate CTA buttons"""
        if 'cta_button' not in spec.features:
            return ''

        secondary = '''<a href="/login" className="btn btn-secondary">Login</a>
            ''' if 'secondary_cta' in spec.features else ''

        return f'''{secondary}<a href="/signup" className="btn btn-primary">Get Started</a>'''

    def _generate_mobile_toggle(self) -> str:
        """Generate mobile menu toggle button"""
        return '''<button className="mobile-toggle" onClick={toggleMenu}>
            {isMenuOpen ? <FiX /> : <FiMenu />}
          </button>'''

    def _generate_scroll_effect(self, spec: TemplateSpec) -> str:
        """Generate scroll effect logic"""
        return '''
  React.useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);'''

    def _is_valid_combination(self, spec: TemplateSpec) -> bool:
        """Validate header combinations"""
        if not super()._is_valid_combination(spec):
            return False

        # Must have logo and nav_links
        if 'logo' not in spec.features or 'nav_links' not in spec.features:
            return False

        # Can't have both dropdown and mega menu
        if 'dropdown_menu' in spec.features and 'mega_menu' in spec.features:
            return False

        # Sticky requires scroll effect or mobile menu
        if 'sticky' in spec.features and 'scroll_effect' not in spec.features:
            # It's okay, sticky can work without scroll effect
            pass

        return True


# ============================================================================
# FOOTER GENERATOR
# ============================================================================

class FooterGenerator(BaseTemplateGenerator):
    """Generates footer templates"""

    def get_domain(self) -> str:
        return "navigation"

    def get_category(self) -> str:
        return "footer"

    def get_variation_config(self) -> VariationConfig:
        """Define footer variations"""
        return VariationConfig(
            styles=[
                'modern',
                'minimal',
                'gradient',
                'dark',
                'professional',
                'creative'
            ],
            layouts=[
                'columns',
                'centered',
                'stacked',
                'minimal',
                'mega'
            ],
            features=[
                # Basic
                ['links', 'copyright'],
                ['links', 'social_icons', 'copyright'],
                ['links', 'logo', 'social_icons', 'copyright'],

                # Newsletter
                ['links', 'newsletter', 'social_icons', 'copyright'],
                ['links', 'logo', 'newsletter', 'social_icons', 'copyright'],

                # Full featured
                ['links', 'logo', 'newsletter', 'social_icons', 'contact_info', 'copyright'],
                ['links', 'logo', 'newsletter', 'social_icons', 'contact_info', 'app_links', 'copyright'],

                # Legal
                ['links', 'social_icons', 'legal_links', 'copyright'],
                ['links', 'logo', 'legal_links', 'privacy_policy', 'terms', 'copyright'],

                # App download
                ['links', 'app_download_buttons', 'social_icons', 'copyright'],
            ],
            animations=['none', 'fade'],
            complexities=['simple', 'standard', 'advanced']
        )

    def generate_code(self, spec: TemplateSpec) -> str:
        """Generate footer component"""
        component_name = spec.get_name()

        imports = "import React from 'react'"
        imports += "\nimport { FaFacebook, FaTwitter, FaLinkedin, FaInstagram, FaGithub } from 'react-icons/fa'"
        imports += "\nimport { FiMail, FiPhone, FiMapPin } from 'react-icons/fi'"

        # Build newsletter state and handler
        newsletter_state = ""
        newsletter_handler = ""
        if 'newsletter' in spec.features:
            newsletter_state = "const [email, setEmail] = React.useState('');"
            newsletter_handler = "const handleNewsletterSubmit = (e) => { e.preventDefault(); console.log('Newsletter signup:', email); };"

        code = f'''{imports}

/**
 * {component_name} Component
 */
const {component_name} = () => {{
  {newsletter_state}

  {newsletter_handler}

  return (
    <footer className="{spec.layout}-layout {spec.style}-style {component_name.lower()}">
      <div className="footer-container">
'''

        if spec.layout == 'columns':
            code += self._generate_columns_layout(spec)
        elif spec.layout == 'centered':
            code += self._generate_centered_layout(spec)
        elif spec.layout == 'stacked':
            code += self._generate_stacked_layout(spec)
        else:
            code += self._generate_default_footer_layout(spec)

        code += '''      </div>

      <div className="footer-bottom">
        <p>&copy; {new Date().getFullYear()} Company Name. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default {component_name};
'''.format(component_name=component_name)

        return code

    def _generate_columns_layout(self, spec: TemplateSpec) -> str:
        """Generate multi-column footer layout"""
        return f'''        <div className="footer-columns">
          <div className="footer-column">
            {'<img src="/logo.svg" alt="Logo" className="footer-logo" />' if 'logo' in spec.features else '<h3>Company</h3>'}
            <p>Building amazing products for amazing people.</p>
            {self._generate_social_icons() if 'social_icons' in spec.features else ''}
          </div>

          <div className="footer-column">
            <h4>Product</h4>
            <ul>
              <li><a href="/features">Features</a></li>
              <li><a href="/pricing">Pricing</a></li>
              <li><a href="/security">Security</a></li>
            </ul>
          </div>

          <div className="footer-column">
            <h4>Company</h4>
            <ul>
              <li><a href="/about">About</a></li>
              <li><a href="/blog">Blog</a></li>
              <li><a href="/careers">Careers</a></li>
            </ul>
          </div>

          <div className="footer-column">
            {self._generate_newsletter(spec) if 'newsletter' in spec.features else '<h4>Support</h4><ul><li><a href="/help">Help Center</a></li></ul>'}
          </div>
        </div>'''

    def _generate_centered_layout(self, spec: TemplateSpec) -> str:
        """Generate centered footer layout"""
        return f'''        <div className="footer-centered">
          {'<img src="/logo.svg" alt="Logo" className="footer-logo" />' if 'logo' in spec.features else ''}

          {self._generate_footer_links()}

          {self._generate_social_icons() if 'social_icons' in spec.features else ''}

          {self._generate_newsletter(spec) if 'newsletter' in spec.features else ''}
        </div>'''

    def _generate_stacked_layout(self, spec: TemplateSpec) -> str:
        """Generate stacked footer layout"""
        return f'''        <div className="footer-stacked">
          {self._generate_newsletter(spec) if 'newsletter' in spec.features else ''}

          <div className="footer-content">
            {self._generate_footer_links()}
            {self._generate_social_icons() if 'social_icons' in spec.features else ''}
          </div>
        </div>'''

    def _generate_default_footer_layout(self, spec: TemplateSpec) -> str:
        """Generate default footer layout"""
        return self._generate_columns_layout(spec)

    def _generate_footer_links(self) -> str:
        """Generate footer navigation links"""
        return '''<nav className="footer-links">
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
            <a href="/privacy">Privacy</a>
            <a href="/terms">Terms</a>
          </nav>'''

    def _generate_social_icons(self) -> str:
        """Generate social media icons"""
        return '''<div className="social-icons">
            <a href="#" aria-label="Facebook"><FaFacebook /></a>
            <a href="#" aria-label="Twitter"><FaTwitter /></a>
            <a href="#" aria-label="LinkedIn"><FaLinkedin /></a>
            <a href="#" aria-label="Instagram"><FaInstagram /></a>
          </div>'''

    def _generate_newsletter(self, spec: TemplateSpec) -> str:
        """Generate newsletter signup"""
        return '''<div className="newsletter">
            <h4>Subscribe to our newsletter</h4>
            <form onSubmit={handleNewsletterSubmit}>
              <input
                type="email"
                placeholder="Enter your email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
              <button type="submit">Subscribe</button>
            </form>
          </div>'''


# ============================================================================
# SIDEBAR GENERATOR
# ============================================================================

class SidebarGenerator(BaseTemplateGenerator):
    """Generates sidebar navigation templates"""

    def get_domain(self) -> str:
        return "navigation"

    def get_category(self) -> str:
        return "sidebar"

    def get_variation_config(self) -> VariationConfig:
        """Define sidebar variations"""
        return VariationConfig(
            styles=[
                'modern',
                'minimal',
                'dark',
                'light',
                'colorful'
            ],
            layouts=[
                'fixed',
                'collapsible',
                'overlay',
                'mini'
            ],
            features=[
                ['nav_items'],
                ['nav_items', 'icons'],
                ['nav_items', 'icons', 'badges'],
                ['nav_items', 'icons', 'nested_menu'],
                ['nav_items', 'icons', 'search'],
                ['nav_items', 'icons', 'user_profile'],
                ['nav_items', 'icons', 'user_profile', 'logout'],
            ],
            animations=['none', 'slide', 'fade'],
            complexities=['simple', 'standard']
        )

    def generate_code(self, spec: TemplateSpec) -> str:
        """Generate sidebar component"""
        component_name = spec.get_name()

        code = f'''import React from 'react'
import {{ FiHome, FiUsers, FiSettings, FiLogOut, FiSearch }} from 'react-icons/fi'

const {component_name} = ({{ isOpen, onClose }}) => {{
  return (
    <aside className="{{`sidebar {spec.layout}-layout {spec.style}-style ${{isOpen ? 'open' : ''}}`}}">
      <div className="sidebar-header">
        <img src="/logo.svg" alt="Logo" />
      </div>

      <nav className="sidebar-nav">
        <a href="/dashboard" className="nav-item active">
          <FiHome /> <span>Dashboard</span>
        </a>
        <a href="/users" className="nav-item">
          <FiUsers /> <span>Users</span>
        </a>
        <a href="/settings" className="nav-item">
          <FiSettings /> <span>Settings</span>
        </a>
      </nav>

      <div className="sidebar-footer">
        <button className="nav-item">
          <FiLogOut /> <span>Logout</span>
        </button>
      </div>
    </aside>
  );
}};

export default {component_name};
'''
        return code
