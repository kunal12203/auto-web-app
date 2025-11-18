"""
Extended Template Generator - Create additional component variants
"""

from pathlib import Path

COMPONENTS_DIR = Path(__file__).parent / "templates" / "components"

# Additional Hero variants
HERO_TEMPLATES = {
    "HeroVideo": '''export default function Hero() {
  return (
    <section className="hero hero-video" id="home">
      <div className="hero-video-bg">
        <div className="hero-overlay">
          <div className="hero-content">
            <h1>{{HERO_HEADLINE}}</h1>
            <p>{{HERO_SUBHEADLINE}}</p>
            <div className="hero-buttons">
              <button className="btn-primary">{{CTA_PRIMARY}}</button>
              <button className="btn-secondary">{{CTA_SECONDARY}}</button>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}''',

    "HeroSplit": '''export default function Hero() {
  return (
    <section className="hero hero-split" id="home">
      <div className="container">
        <div className="hero-split-container">
          <div className="hero-split-content">
            <h1>{{HERO_HEADLINE}}</h1>
            <p>{{HERO_SUBHEADLINE}}</p>
            <button className="btn-primary">{{CTA_PRIMARY}}</button>
          </div>
          <div className="hero-split-image">
            <div className="hero-image-placeholder">{{HERO_ICON}}</div>
          </div>
        </div>
      </div>
    </section>
  )
}''',

    "HeroWithForm": '''import { useState } from 'react'

export default function Hero() {
  const [email, setEmail] = useState('')

  return (
    <section className="hero hero-with-form" id="home">
      <div className="container">
        <h1>{{HERO_HEADLINE}}</h1>
        <p>{{HERO_SUBHEADLINE}}</p>
        <form onSubmit={(e) => e.preventDefault()} className="hero-form">
          <input
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <button type="submit">{{CTA_PRIMARY}}</button>
        </form>
        <p className="hero-note">{{HERO_NOTE}}</p>
      </div>
    </section>
  )
}''',

    "HeroWithStats": '''export default function Hero() {
  const stats = [
    { value: '{{STAT_1_VALUE}}', label: '{{STAT_1_LABEL}}' },
    { value: '{{STAT_2_VALUE}}', label: '{{STAT_2_LABEL}}' },
    { value: '{{STAT_3_VALUE}}', label: '{{STAT_3_LABEL}}' }
  ]

  return (
    <section className="hero hero-with-stats" id="home">
      <div className="container">
        <h1>{{HERO_HEADLINE}}</h1>
        <p>{{HERO_SUBHEADLINE}}</p>
        <div className="hero-stats">
          {stats.map((stat, i) => (
            <div key={i} className="hero-stat">
              <div className="stat-value">{stat.value}</div>
              <div className="stat-label">{stat.label}</div>
            </div>
          ))}
        </div>
        <button className="btn-primary">{{CTA_PRIMARY}}</button>
      </div>
    </section>
  )
}''',

    "HeroGradient": '''export default function Hero() {
  return (
    <section className="hero hero-gradient" id="home">
      <div className="hero-gradient-bg">
        <div className="container">
          <h1>{{HERO_HEADLINE}}</h1>
          <p>{{HERO_SUBHEADLINE}}</p>
          <div className="hero-buttons">
            <button className="btn-primary">{{CTA_PRIMARY}}</button>
            <button className="btn-secondary">{{CTA_SECONDARY}}</button>
          </div>
        </div>
      </div>
    </section>
  )
}''',

    "HeroAnimated": '''export default function Hero() {
  return (
    <section className="hero hero-animated" id="home">
      <div className="container">
        <div className="hero-animated-content">
          <h1 className="hero-fade-in">{{HERO_HEADLINE}}</h1>
          <p className="hero-fade-in-delay">{{HERO_SUBHEADLINE}}</p>
          <div className="hero-buttons hero-fade-in-delay-2">
            <button className="btn-primary">{{CTA_PRIMARY}}</button>
          </div>
        </div>
      </div>
    </section>
  )
}''',

    "HeroFullHeight": '''export default function Hero() {
  return (
    <section className="hero hero-full-height" id="home">
      <div className="hero-full-content">
        <h1>{{HERO_HEADLINE}}</h1>
        <p>{{HERO_SUBHEADLINE}}</p>
        <button className="btn-primary">{{CTA_PRIMARY}}</button>
        <div className="hero-scroll-indicator">
          <span>Scroll Down ↓</span>
        </div>
      </div>
    </section>
  )
}'''
}

# Additional Header variants
HEADER_TEMPLATES = {
    "HeaderTransparent": '''import { useState } from 'react'

export default function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  return (
    <header className="header header-transparent">
      <div className="container">
        <div className="logo">{{BRAND_NAME}}</div>
        <nav className={isMenuOpen ? 'nav-open' : ''}>
          <a href="#home">Home</a>
          <a href="#about">About</a>
          <a href="#services">Services</a>
          <a href="#contact">Contact</a>
        </nav>
        <button
          className="menu-toggle"
          onClick={() => setIsMenuOpen(!isMenuOpen)}
        >
          ☰
        </button>
      </div>
    </header>
  )
}''',

    "HeaderWithSearch": '''import { useState } from 'react'

export default function Header() {
  const [searchOpen, setSearchOpen] = useState(false)

  return (
    <header className="header header-with-search">
      <div className="container">
        <div className="logo">{{BRAND_NAME}}</div>
        <nav>
          <a href="#home">Home</a>
          <a href="#products">Products</a>
          <a href="#about">About</a>
          <a href="#contact">Contact</a>
        </nav>
        <div className="header-actions">
          <button onClick={() => setSearchOpen(!searchOpen)}>🔍</button>
          <button className="cta-button">Get Started</button>
        </div>
        {searchOpen && (
          <div className="search-bar">
            <input type="search" placeholder="Search..." />
          </div>
        )}
      </div>
    </header>
  )
}''',

    "HeaderCentered": '''export default function Header() {
  return (
    <header className="header header-centered">
      <div className="container">
        <div className="header-centered-content">
          <div className="logo">{{BRAND_NAME}}</div>
          <nav>
            <a href="#home">Home</a>
            <a href="#work">Work</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
          </nav>
        </div>
      </div>
    </header>
  )
}''',

    "HeaderWithAuth": '''import { useState } from 'react'

export default function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  return (
    <header className="header header-with-auth">
      <div className="container">
        <div className="logo">{{BRAND_NAME}}</div>
        <nav className={isMenuOpen ? 'nav-open' : ''}>
          <a href="#features">Features</a>
          <a href="#pricing">Pricing</a>
          <a href="#about">About</a>
        </nav>
        <div className="header-auth">
          <button className="btn-ghost">Sign In</button>
          <button className="cta-button">Sign Up</button>
        </div>
        <button
          className="menu-toggle"
          onClick={() => setIsMenuOpen(!isMenuOpen)}
        >
          ☰
        </button>
      </div>
    </header>
  )
}''',

    "HeaderMegaMenu": '''import { useState } from 'react'

export default function Header() {
  const [megaMenuOpen, setMegaMenuOpen] = useState(false)

  return (
    <header className="header header-mega-menu">
      <div className="container">
        <div className="logo">{{BRAND_NAME}}</div>
        <nav>
          <a href="#home">Home</a>
          <a
            href="#products"
            onMouseEnter={() => setMegaMenuOpen(true)}
            onMouseLeave={() => setMegaMenuOpen(false)}
          >
            Products
          </a>
          <a href="#pricing">Pricing</a>
          <a href="#contact">Contact</a>
        </nav>
        {megaMenuOpen && (
          <div
            className="mega-menu"
            onMouseEnter={() => setMegaMenuOpen(true)}
            onMouseLeave={() => setMegaMenuOpen(false)}
          >
            <div className="mega-menu-content">
              <div className="mega-menu-column">
                <h4>Category 1</h4>
                <a href="#">Product A</a>
                <a href="#">Product B</a>
              </div>
              <div className="mega-menu-column">
                <h4>Category 2</h4>
                <a href="#">Product C</a>
                <a href="#">Product D</a>
              </div>
            </div>
          </div>
        )}
        <button className="cta-button">Get Started</button>
      </div>
    </header>
  )
}''',

    "HeaderSticky": '''import { useState, useEffect } from 'react'

export default function Header() {
  const [isSticky, setIsSticky] = useState(false)

  useEffect(() => {
    const handleScroll = () => {
      setIsSticky(window.scrollY > 100)
    }
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  return (
    <header className={`header header-sticky ${isSticky ? 'sticky' : ''}`}>
      <div className="container">
        <div className="logo">{{BRAND_NAME}}</div>
        <nav>
          <a href="#home">Home</a>
          <a href="#services">Services</a>
          <a href="#about">About</a>
          <a href="#contact">Contact</a>
        </nav>
        <button className="cta-button">Get Started</button>
      </div>
    </header>
  )
}'''
}

# Additional Footer variants
FOOTER_TEMPLATES = {
    "FooterSimple": '''export default function Footer() {
  return (
    <footer className="footer footer-simple">
      <div className="container">
        <div className="footer-simple-content">
          <p>&copy; 2024 {{BRAND_NAME}}. All rights reserved.</p>
          <div className="footer-links">
            <a href="#">Privacy</a>
            <a href="#">Terms</a>
            <a href="#">Contact</a>
          </div>
        </div>
      </div>
    </footer>
  )
}''',

    "FooterNewsletter": '''import { useState } from 'react'

export default function Footer() {
  return (
    <footer className="footer footer-newsletter">
      <div className="container">
        <div className="footer-newsletter-section">
          <h3>{{NEWSLETTER_HEADLINE}}</h3>
          <form onSubmit={(e) => e.preventDefault()} className="footer-newsletter-form">
            <input type="email" placeholder="Your email" />
            <button type="submit">Subscribe</button>
          </form>
        </div>
        <div className="footer-grid">
          <div className="footer-col">
            <h4>{{BRAND_NAME}}</h4>
            <p>{{BRAND_TAGLINE}}</p>
          </div>
          <div className="footer-col">
            <h4>Quick Links</h4>
            <a href="#">About</a>
            <a href="#">Services</a>
            <a href="#">Contact</a>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; 2024 {{BRAND_NAME}}. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}''',

    "FooterLarge": '''export default function Footer() {
  return (
    <footer className="footer footer-large">
      <div className="container">
        <div className="footer-large-grid">
          <div className="footer-col-large">
            <h4>{{BRAND_NAME}}</h4>
            <p>{{BRAND_TAGLINE}}</p>
            <div className="footer-social-large">
              <a href="#">Facebook</a>
              <a href="#">Twitter</a>
              <a href="#">Instagram</a>
              <a href="#">LinkedIn</a>
            </div>
          </div>
          <div className="footer-col">
            <h4>Products</h4>
            <a href="#">Product 1</a>
            <a href="#">Product 2</a>
            <a href="#">Product 3</a>
          </div>
          <div className="footer-col">
            <h4>Company</h4>
            <a href="#">About Us</a>
            <a href="#">Careers</a>
            <a href="#">Blog</a>
          </div>
          <div className="footer-col">
            <h4>Support</h4>
            <a href="#">Help Center</a>
            <a href="#">Contact</a>
            <a href="#">FAQ</a>
          </div>
          <div className="footer-col">
            <h4>Legal</h4>
            <a href="#">Privacy Policy</a>
            <a href="#">Terms of Service</a>
            <a href="#">Cookie Policy</a>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; 2024 {{BRAND_NAME}}. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}''',

    "FooterCentered": '''export default function Footer() {
  return (
    <footer className="footer footer-centered">
      <div className="container">
        <div className="footer-centered-content">
          <div className="logo">{{BRAND_NAME}}</div>
          <nav className="footer-nav">
            <a href="#">Home</a>
            <a href="#">About</a>
            <a href="#">Services</a>
            <a href="#">Contact</a>
          </nav>
          <div className="footer-social">
            <a href="#">Facebook</a>
            <a href="#">Twitter</a>
            <a href="#">Instagram</a>
          </div>
          <p>&copy; 2024 {{BRAND_NAME}}. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}''',

    "FooterWithMap": '''export default function Footer() {
  return (
    <footer className="footer footer-with-map">
      <div className="container">
        <div className="footer-map-grid">
          <div className="footer-info">
            <h4>{{BRAND_NAME}}</h4>
            <p>📍 {{CONTACT_ADDRESS}}</p>
            <p>📞 {{CONTACT_PHONE}}</p>
            <p>📧 {{CONTACT_EMAIL}}</p>
          </div>
          <div className="footer-map">
            <div className="map-placeholder">🗺️ Map</div>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; 2024 {{BRAND_NAME}}. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}''',

    "FooterDark": '''export default function Footer() {
  return (
    <footer className="footer footer-dark">
      <div className="container">
        <div className="footer-grid">
          <div className="footer-col">
            <h4>{{BRAND_NAME}}</h4>
            <p>{{BRAND_TAGLINE}}</p>
          </div>
          <div className="footer-col">
            <h4>Company</h4>
            <a href="#">About</a>
            <a href="#">Team</a>
            <a href="#">Careers</a>
          </div>
          <div className="footer-col">
            <h4>Resources</h4>
            <a href="#">Blog</a>
            <a href="#">Help Center</a>
            <a href="#">Contact</a>
          </div>
          <div className="footer-col">
            <h4>Connect</h4>
            <a href="#">Facebook</a>
            <a href="#">Twitter</a>
            <a href="#">LinkedIn</a>
          </div>
        </div>
        <div className="footer-bottom-dark">
          <p>&copy; 2024 {{BRAND_NAME}}. All rights reserved.</p>
          <div className="footer-legal">
            <a href="#">Privacy Policy</a>
            <a href="#">Terms of Service</a>
          </div>
        </div>
      </div>
    </footer>
  )
}'''
}

def generate_all_templates():
    """Generate all extended template files"""

    categories = {
        'heroes': HERO_TEMPLATES,
        'headers': HEADER_TEMPLATES,
        'footers': FOOTER_TEMPLATES
    }

    total = 0
    for category, templates in categories.items():
        category_dir = COMPONENTS_DIR / category
        category_dir.mkdir(parents=True, exist_ok=True)

        for name, content in templates.items():
            file_path = category_dir / f"{name}.jsx"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Created {category}/{name}.jsx")
            total += 1

    print(f"\n✅ Generated {total} additional template files!")

if __name__ == "__main__":
    generate_all_templates()
