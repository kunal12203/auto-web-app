"""
Component Templates for Common Website Types
Pre-built, high-quality components to reduce AI generation and improve consistency
"""

# Template-based components with placeholders for AI-generated content
COMPONENT_TEMPLATES = {
    "fitness": {
        "components": ["Header", "Hero", "Services", "Pricing", "Testimonials", "Footer"],
        "templates": {
            "Header": """import { useState } from 'react'

export default function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  return (
    <header className="header">
      <div className="container">
        <div className="logo">{{GYM_NAME}}</div>
        <nav className={isMenuOpen ? 'nav-open' : ''}>
          <a href="#home">Home</a>
          <a href="#services">Services</a>
          <a href="#pricing">Pricing</a>
          <a href="#testimonials">Testimonials</a>
          <a href="#contact">Contact</a>
        </nav>
        <button className="cta-button">Join Now</button>
        <button className="menu-toggle" onClick={() => setIsMenuOpen(!isMenuOpen)}>
          ☰
        </button>
      </div>
    </header>
  )
}""",
            "Hero": """export default function Hero() {
  return (
    <section className="hero" id="home">
      <div className="hero-content">
        <h1>{{HERO_TITLE}}</h1>
        <p>{{HERO_SUBTITLE}}</p>
        <div className="hero-buttons">
          <button className="btn-primary">Start Free Trial</button>
          <button className="btn-secondary">View Classes</button>
        </div>
      </div>
      <div className="hero-image">
        <div className="placeholder-image">🏋️</div>
      </div>
    </section>
  )
}""",
            "Services": """const services = {{SERVICES_ARRAY}}

export default function Services() {
  return (
    <section className="services" id="services">
      <h2>Our Services</h2>
      <div className="services-grid">
        {services.map((service, index) => (
          <div key={index} className="service-card">
            <div className="service-icon">{service.icon}</div>
            <h3>{service.title}</h3>
            <p>{service.description}</p>
          </div>
        ))}
      </div>
    </section>
  )
}""",
            "Pricing": """const plans = {{PRICING_ARRAY}}

export default function Pricing() {
  return (
    <section className="pricing" id="pricing">
      <h2>Membership Plans</h2>
      <div className="pricing-grid">
        {plans.map((plan, index) => (
          <div key={index} className={`pricing-card ${plan.featured ? 'featured' : ''}`}>
            <h3>{plan.name}</h3>
            <div className="price">
              <span className="amount">${plan.price}</span>
              <span className="period">/month</span>
            </div>
            <ul className="features">
              {plan.features.map((feature, i) => (
                <li key={i}>✓ {feature}</li>
              ))}
            </ul>
            <button className="btn-primary">Choose Plan</button>
          </div>
        ))}
      </div>
    </section>
  )
}""",
            "Testimonials": """const testimonials = {{TESTIMONIALS_ARRAY}}

export default function Testimonials() {
  return (
    <section className="testimonials" id="testimonials">
      <h2>What Our Members Say</h2>
      <div className="testimonials-grid">
        {testimonials.map((testimonial, index) => (
          <div key={index} className="testimonial-card">
            <p className="quote">"{testimonial.quote}"</p>
            <div className="author">
              <strong>{testimonial.name}</strong>
              <span>{testimonial.role}</span>
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}""",
            "Footer": """export default function Footer() {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-grid">
          <div className="footer-col">
            <h4>{{GYM_NAME}}</h4>
            <p>{{GYM_DESCRIPTION}}</p>
          </div>
          <div className="footer-col">
            <h4>Quick Links</h4>
            <a href="#home">Home</a>
            <a href="#services">Services</a>
            <a href="#pricing">Pricing</a>
            <a href="#contact">Contact</a>
          </div>
          <div className="footer-col">
            <h4>Contact</h4>
            <p>📧 {{EMAIL}}</p>
            <p>📞 {{PHONE}}</p>
            <p>📍 {{ADDRESS}}</p>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; 2024 {{GYM_NAME}}. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}"""
        }
    },
    "ecommerce": {
        "components": ["Header", "Hero", "ProductGrid", "Features", "Newsletter", "Footer"],
        "templates": {
            "Header": """import { useState } from 'react'

export default function Header() {
  const [cartCount, setCartCount] = useState(0)

  return (
    <header className="header">
      <div className="container">
        <div className="logo">{{STORE_NAME}}</div>
        <nav>
          <a href="#home">Home</a>
          <a href="#products">Products</a>
          <a href="#about">About</a>
          <a href="#contact">Contact</a>
        </nav>
        <div className="header-actions">
          <button className="cart-button">🛒 ({cartCount})</button>
        </div>
      </div>
    </header>
  )
}""",
            "ProductGrid": """const products = {{PRODUCTS_ARRAY}}

export default function ProductGrid() {
  return (
    <section className="products" id="products">
      <h2>Our Products</h2>
      <div className="product-grid">
        {products.map((product, index) => (
          <div key={index} className="product-card">
            <div className="product-image">{product.icon || '📦'}</div>
            <h3>{product.name}</h3>
            <p>{product.description}</p>
            <div className="product-footer">
              <span className="price">${product.price}</span>
              <button className="btn-primary">Add to Cart</button>
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}"""
        }
    },
    "restaurant": {
        "components": ["Header", "Hero", "Menu", "About", "Reservation", "Footer"],
        "templates": {
            "Menu": """const menuItems = {{MENU_ARRAY}}

export default function Menu() {
  return (
    <section className="menu" id="menu">
      <h2>Our Menu</h2>
      <div className="menu-grid">
        {menuItems.map((item, index) => (
          <div key={index} className="menu-item">
            <div className="item-header">
              <h3>{item.name}</h3>
              <span className="price">${item.price}</span>
            </div>
            <p>{item.description}</p>
          </div>
        ))}
      </div>
    </section>
  )
}"""
        }
    }
}


def detect_website_type(prompt: str) -> str:
    """Detect website type from user prompt"""
    prompt_lower = prompt.lower()

    # Fitness/Gym keywords
    if any(word in prompt_lower for word in ['gym', 'fitness', 'workout', 'training', 'exercise', 'yoga', 'crossfit']):
        return 'fitness'

    # E-commerce keywords
    if any(word in prompt_lower for word in ['shop', 'store', 'ecommerce', 'e-commerce', 'product', 'cart', 'checkout']):
        return 'ecommerce'

    # Restaurant keywords
    if any(word in prompt_lower for word in ['restaurant', 'cafe', 'food', 'menu', 'dining', 'reservation']):
        return 'restaurant'

    return None


def get_template_components(website_type: str) -> dict:
    """Get pre-built component templates for a website type"""
    return COMPONENT_TEMPLATES.get(website_type, {})
