"""
Specialized Template Generator - E-commerce, SaaS, Restaurant, Cards, and more
"""

from pathlib import Path

COMPONENTS_DIR = Path(__file__).parent / "templates" / "components"

# E-commerce Components
ECOMMERCE_TEMPLATES = {
    "ProductGrid": '''export default function ProductGrid() {
  const products = [
    { name: '{{PRODUCT_1_NAME}}', price: '{{PRODUCT_1_PRICE}}', image: '{{PRODUCT_1_ICON}}', rating: '{{PRODUCT_1_RATING}}' },
    { name: '{{PRODUCT_2_NAME}}', price: '{{PRODUCT_2_PRICE}}', image: '{{PRODUCT_2_ICON}}', rating: '{{PRODUCT_2_RATING}}' },
    { name: '{{PRODUCT_3_NAME}}', price: '{{PRODUCT_3_PRICE}}', image: '{{PRODUCT_3_ICON}}', rating: '{{PRODUCT_3_RATING}}' },
    { name: '{{PRODUCT_4_NAME}}', price: '{{PRODUCT_4_PRICE}}', image: '{{PRODUCT_4_ICON}}', rating: '{{PRODUCT_4_RATING}}' }
  ]

  return (
    <section className="products product-grid">
      <div className="container">
        <h2>{{PRODUCTS_HEADLINE}}</h2>
        <div className="product-grid-container">
          {products.map((product, i) => (
            <div key={i} className="product-card">
              <div className="product-image">{product.image}</div>
              <h3>{product.name}</h3>
              <div className="product-rating">⭐ {product.rating}</div>
              <div className="product-price">${product.price}</div>
              <button className="add-to-cart">Add to Cart</button>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "ProductShowcase": '''export default function ProductShowcase() {
  return (
    <section className="product-showcase">
      <div className="container">
        <div className="showcase-grid">
          <div className="showcase-image">
            <div className="product-image-large">{{PRODUCT_ICON}}</div>
          </div>
          <div className="showcase-info">
            <h2>{{PRODUCT_NAME}}</h2>
            <div className="product-rating">⭐⭐⭐⭐⭐ ({{PRODUCT_REVIEWS}} reviews)</div>
            <div className="product-price-large">${{PRODUCT_PRICE}}</div>
            <p>{{PRODUCT_DESCRIPTION}}</p>
            <div className="product-features">
              <ul>
                <li>{{FEATURE_1}}</li>
                <li>{{FEATURE_2}}</li>
                <li>{{FEATURE_3}}</li>
              </ul>
            </div>
            <button className="btn-primary">Buy Now</button>
          </div>
        </div>
      </div>
    </section>
  )
}''',

    "ProductCarousel": '''import { useState } from 'react'

export default function ProductCarousel() {
  const [currentIndex, setCurrentIndex] = useState(0)
  
  const products = [
    { name: '{{PRODUCT_1_NAME}}', price: '{{PRODUCT_1_PRICE}}', image: '{{PRODUCT_1_ICON}}' },
    { name: '{{PRODUCT_2_NAME}}', price: '{{PRODUCT_2_PRICE}}', image: '{{PRODUCT_2_ICON}}' },
    { name: '{{PRODUCT_3_NAME}}', price: '{{PRODUCT_3_PRICE}}', image: '{{PRODUCT_3_ICON}}' }
  ]

  return (
    <section className="product-carousel">
      <div className="container">
        <h2>{{CAROUSEL_HEADLINE}}</h2>
        <div className="carousel-container">
          <button onClick={() => setCurrentIndex(Math.max(0, currentIndex - 1))}>←</button>
          <div className="carousel-item">
            <div className="product-image">{products[currentIndex].image}</div>
            <h3>{products[currentIndex].name}</h3>
            <p>${products[currentIndex].price}</p>
          </div>
          <button onClick={() => setCurrentIndex(Math.min(products.length - 1, currentIndex + 1))}>→</button>
        </div>
      </div>
    </section>
  )
}''',

    "ProductReviews": '''export default function ProductReviews() {
  const reviews = [
    { author: '{{REVIEW_1_AUTHOR}}', rating: '{{REVIEW_1_RATING}}', text: '{{REVIEW_1_TEXT}}', date: '{{REVIEW_1_DATE}}' },
    { author: '{{REVIEW_2_AUTHOR}}', rating: '{{REVIEW_2_RATING}}', text: '{{REVIEW_2_TEXT}}', date: '{{REVIEW_2_DATE}}' },
    { author: '{{REVIEW_3_AUTHOR}}', rating: '{{REVIEW_3_RATING}}', text: '{{REVIEW_3_TEXT}}', date: '{{REVIEW_3_DATE}}' }
  ]

  return (
    <section className="product-reviews">
      <div className="container">
        <h2>Customer Reviews</h2>
        <div className="reviews-list">
          {reviews.map((review, i) => (
            <div key={i} className="review-card">
              <div className="review-header">
                <strong>{review.author}</strong>
                <span>{'⭐'.repeat(parseInt(review.rating))}</span>
              </div>
              <p>{review.text}</p>
              <span className="review-date">{review.date}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "CartSummary": '''import { useState } from 'react'

export default function CartSummary() {
  const [items] = useState([
    { name: '{{CART_ITEM_1}}', price: '{{CART_PRICE_1}}', quantity: 1 },
    { name: '{{CART_ITEM_2}}', price: '{{CART_PRICE_2}}', quantity: 2 }
  ])

  const total = items.reduce((sum, item) => sum + (parseFloat(item.price) * item.quantity), 0)

  return (
    <section className="cart-summary">
      <div className="container">
        <h2>Your Cart</h2>
        <div className="cart-items">
          {items.map((item, i) => (
            <div key={i} className="cart-item">
              <span>{item.name}</span>
              <span>Qty: {item.quantity}</span>
              <span>${item.price}</span>
            </div>
          ))}
        </div>
        <div className="cart-total">
          <strong>Total:</strong>
          <strong>${total.toFixed(2)}</strong>
        </div>
        <button className="btn-primary">Proceed to Checkout</button>
      </div>
    </section>
  )
}'''
}

# SaaS Components
SAAS_TEMPLATES = {
    "FeatureComparison": '''export default function FeatureComparison() {
  const features = [
    { name: '{{FEATURE_1}}', basic: true, pro: true, enterprise: true },
    { name: '{{FEATURE_2}}', basic: true, pro: true, enterprise: true },
    { name: '{{FEATURE_3}}', basic: false, pro: true, enterprise: true },
    { name: '{{FEATURE_4}}', basic: false, pro: false, enterprise: true }
  ]

  return (
    <section className="feature-comparison">
      <div className="container">
        <h2>Compare Plans</h2>
        <table className="comparison-table">
          <thead>
            <tr>
              <th>Feature</th>
              <th>Basic</th>
              <th>Pro</th>
              <th>Enterprise</th>
            </tr>
          </thead>
          <tbody>
            {features.map((feature, i) => (
              <tr key={i}>
                <td>{feature.name}</td>
                <td>{feature.basic ? '✓' : '—'}</td>
                <td>{feature.pro ? '✓' : '—'}</td>
                <td>{feature.enterprise ? '✓' : '—'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  )
}''',

    "IntegrationLogos": '''export default function IntegrationLogos() {
  const integrations = [
    '{{INTEGRATION_1}}', '{{INTEGRATION_2}}', '{{INTEGRATION_3}}',
    '{{INTEGRATION_4}}', '{{INTEGRATION_5}}', '{{INTEGRATION_6}}'
  ]

  return (
    <section className="integrations">
      <div className="container">
        <h2>Integrates With Your Favorite Tools</h2>
        <div className="integration-grid">
          {integrations.map((integration, i) => (
            <div key={i} className="integration-logo">
              {integration}
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "Dashboard Preview": '''export default function DashboardPreview() {
  return (
    <section className="dashboard-preview">
      <div className="container">
        <h2>{{DASHBOARD_HEADLINE}}</h2>
        <p>{{DASHBOARD_SUBHEADLINE}}</p>
        <div className="dashboard-mockup">
          <div className="dashboard-placeholder">
            📊 Dashboard Preview
          </div>
        </div>
      </div>
    </section>
  )
}''',

    "APIDocumentation": '''export default function APIDocumentation() {
  const endpoints = [
    { method: 'GET', path: '/api/users', description: '{{API_1_DESC}}' },
    { method: 'POST', path: '/api/users', description: '{{API_2_DESC}}' },
    { method: 'PUT', path: '/api/users/:id', description: '{{API_3_DESC}}' }
  ]

  return (
    <section className="api-docs">
      <div className="container">
        <h2>API Documentation</h2>
        <div className="api-endpoints">
          {endpoints.map((endpoint, i) => (
            <div key={i} className="api-endpoint">
              <span className={`method method-${endpoint.method.toLowerCase()}`}>
                {endpoint.method}
              </span>
              <code>{endpoint.path}</code>
              <p>{endpoint.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}'''
}

# Restaurant Components
RESTAURANT_TEMPLATES = {
    "MenuSection": '''export default function MenuSection() {
  const menuItems = [
    { name: '{{MENU_ITEM_1}}', description: '{{MENU_DESC_1}}', price: '{{MENU_PRICE_1}}' },
    { name: '{{MENU_ITEM_2}}', description: '{{MENU_DESC_2}}', price: '{{MENU_PRICE_2}}' },
    { name: '{{MENU_ITEM_3}}', description: '{{MENU_DESC_3}}', price: '{{MENU_PRICE_3}}' },
    { name: '{{MENU_ITEM_4}}', description: '{{MENU_DESC_4}}', price: '{{MENU_PRICE_4}}' }
  ]

  return (
    <section className="menu-section">
      <div className="container">
        <h2>{{MENU_HEADLINE}}</h2>
        <div className="menu-grid">
          {menuItems.map((item, i) => (
            <div key={i} className="menu-item">
              <div className="menu-item-header">
                <h3>{item.name}</h3>
                <span className="menu-price">${item.price}</span>
              </div>
              <p>{item.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "ReservationForm": '''import { useState } from 'react'

export default function ReservationForm() {
  const [formData, setFormData] = useState({
    name: '', date: '', time: '', guests: 2
  })

  return (
    <section className="reservation-form">
      <div className="container">
        <h2>Make a Reservation</h2>
        <form onSubmit={(e) => e.preventDefault()}>
          <input type="text" placeholder="Name" required />
          <input type="date" required />
          <input type="time" required />
          <select>
            <option>2 guests</option>
            <option>4 guests</option>
            <option>6 guests</option>
          </select>
          <button type="submit" className="btn-primary">Reserve Table</button>
        </form>
      </div>
    </section>
  )
}''',

    "ChefProfile": '''export default function ChefProfile() {
  return (
    <section className="chef-profile">
      <div className="container">
        <div className="chef-grid">
          <div className="chef-image">{{CHEF_ICON}}</div>
          <div className="chef-info">
            <h2>{{CHEF_NAME}}</h2>
            <h3>{{CHEF_TITLE}}</h3>
            <p>{{CHEF_BIO}}</p>
          </div>
        </div>
      </div>
    </section>
  )
}''',

    "HoursLocation": '''export default function HoursLocation() {
  const hours = [
    { day: 'Monday - Friday', time: '{{HOURS_WEEKDAY}}' },
    { day: 'Saturday', time: '{{HOURS_SATURDAY}}' },
    { day: 'Sunday', time: '{{HOURS_SUNDAY}}' }
  ]

  return (
    <section className="hours-location">
      <div className="container">
        <div className="hours-grid">
          <div className="hours">
            <h3>Hours</h3>
            {hours.map((item, i) => (
              <div key={i} className="hours-row">
                <span>{item.day}</span>
                <span>{item.time}</span>
              </div>
            ))}
          </div>
          <div className="location">
            <h3>Location</h3>
            <p>📍 {{CONTACT_ADDRESS}}</p>
            <p>📞 {{CONTACT_PHONE}}</p>
          </div>
        </div>
      </div>
    </section>
  )
}'''
}

# Card Components
CARD_TEMPLATES = {
    "ServiceCards": '''export default function ServiceCards() {
  const services = [
    { icon: '{{SERVICE_1_ICON}}', title: '{{SERVICE_1_TITLE}}', description: '{{SERVICE_1_DESC}}' },
    { icon: '{{SERVICE_2_ICON}}', title: '{{SERVICE_2_TITLE}}', description: '{{SERVICE_2_DESC}}' },
    { icon: '{{SERVICE_3_ICON}}', title: '{{SERVICE_3_TITLE}}', description: '{{SERVICE_3_DESC}}' }
  ]

  return (
    <section className="service-cards">
      <div className="container">
        <div className="cards-grid">
          {services.map((service, i) => (
            <div key={i} className="service-card">
              <div className="card-icon">{service.icon}</div>
              <h3>{service.title}</h3>
              <p>{service.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "IconCards": '''export default function IconCards() {
  const items = [
    { icon: '{{ICON_1}}', title: '{{TITLE_1}}' },
    { icon: '{{ICON_2}}', title: '{{TITLE_2}}' },
    { icon: '{{ICON_3}}', title: '{{TITLE_3}}' },
    { icon: '{{ICON_4}}', title: '{{TITLE_4}}' }
  ]

  return (
    <section className="icon-cards">
      <div className="container">
        <div className="icon-cards-grid">
          {items.map((item, i) => (
            <div key={i} className="icon-card">
              <div className="icon-large">{item.icon}</div>
              <h3>{item.title}</h3>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "InfoCards": '''export default function InfoCards() {
  const cards = [
    { title: '{{CARD_1_TITLE}}', description: '{{CARD_1_DESC}}', link: '{{CARD_1_LINK}}' },
    { title: '{{CARD_2_TITLE}}', description: '{{CARD_2_DESC}}', link: '{{CARD_2_LINK}}' }
  ]

  return (
    <section className="info-cards">
      <div className="container">
        <div className="info-cards-grid">
          {cards.map((card, i) => (
            <div key={i} className="info-card">
              <h3>{card.title}</h3>
              <p>{card.description}</p>
              <a href={card.link} className="card-link">Learn More →</a>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}'''
}

# Logo/Partner Components
LOGO_TEMPLATES = {
    "LogoGrid": '''export default function LogoGrid() {
  const logos = [
    '{{LOGO_1}}', '{{LOGO_2}}', '{{LOGO_3}}',
    '{{LOGO_4}}', '{{LOGO_5}}', '{{LOGO_6}}'
  ]

  return (
    <section className="logo-grid">
      <div className="container">
        <h2>{{LOGOS_HEADLINE}}</h2>
        <div className="logos-container">
          {logos.map((logo, i) => (
            <div key={i} className="logo-item">{logo}</div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "PartnerLogos": '''export default function PartnerLogos() {
  const partners = [
    '{{PARTNER_1}}', '{{PARTNER_2}}', '{{PARTNER_3}}',
    '{{PARTNER_4}}', '{{PARTNER_5}}'
  ]

  return (
    <section className="partner-logos">
      <div className="container">
        <p className="partners-intro">Trusted by</p>
        <div className="partners-grid">
          {partners.map((partner, i) => (
            <div key={i} className="partner-logo">{partner}</div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "ClientLogos": '''export default function ClientLogos() {
  return (
    <section className="client-logos">
      <div className="container">
        <h3>Our Clients</h3>
        <div className="client-logos-scroll">
          <div className="logo-item">{{CLIENT_1}}</div>
          <div className="logo-item">{{CLIENT_2}}</div>
          <div className="logo-item">{{CLIENT_3}}</div>
          <div className="logo-item">{{CLIENT_4}}</div>
        </div>
      </div>
    </section>
  )
}'''
}

# Timeline Components
TIMELINE_TEMPLATES = {
    "TimelineVertical": '''export default function TimelineVertical() {
  const events = [
    { year: '{{TIMELINE_1_YEAR}}', title: '{{TIMELINE_1_TITLE}}', description: '{{TIMELINE_1_DESC}}' },
    { year: '{{TIMELINE_2_YEAR}}', title: '{{TIMELINE_2_TITLE}}', description: '{{TIMELINE_2_DESC}}' },
    { year: '{{TIMELINE_3_YEAR}}', title: '{{TIMELINE_3_TITLE}}', description: '{{TIMELINE_3_DESC}}' }
  ]

  return (
    <section className="timeline timeline-vertical">
      <div className="container">
        <h2>{{TIMELINE_HEADLINE}}</h2>
        <div className="timeline-container">
          {events.map((event, i) => (
            <div key={i} className="timeline-item">
              <div className="timeline-year">{event.year}</div>
              <div className="timeline-content">
                <h3>{event.title}</h3>
                <p>{event.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "ProcessSteps": '''export default function ProcessSteps() {
  const steps = [
    { number: 1, title: '{{STEP_1_TITLE}}', description: '{{STEP_1_DESC}}' },
    { number: 2, title: '{{STEP_2_TITLE}}', description: '{{STEP_2_DESC}}' },
    { number: 3, title: '{{STEP_3_TITLE}}', description: '{{STEP_3_DESC}}' },
    { number: 4, title: '{{STEP_4_TITLE}}', description: '{{STEP_4_DESC}}' }
  ]

  return (
    <section className="process-steps">
      <div className="container">
        <h2>{{PROCESS_HEADLINE}}</h2>
        <div className="steps-grid">
          {steps.map((step, i) => (
            <div key={i} className="step-item">
              <div className="step-number">{step.number}</div>
              <h3>{step.title}</h3>
              <p>{step.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "RoadmapTimeline": '''export default function RoadmapTimeline() {
  const milestones = [
    { quarter: 'Q1 2024', title: '{{MILESTONE_1}}', status: 'completed' },
    { quarter: 'Q2 2024', title: '{{MILESTONE_2}}', status: 'in-progress' },
    { quarter: 'Q3 2024', title: '{{MILESTONE_3}}', status: 'planned' }
  ]

  return (
    <section className="roadmap-timeline">
      <div className="container">
        <h2>Product Roadmap</h2>
        <div className="roadmap">
          {milestones.map((milestone, i) => (
            <div key={i} className={`roadmap-item ${milestone.status}`}>
              <div className="roadmap-quarter">{milestone.quarter}</div>
              <h3>{milestone.title}</h3>
              <span className="status-badge">{milestone.status}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}'''
}

# Video Components
VIDEO_TEMPLATES = {
    "VideoHero": '''export default function VideoHero() {
  return (
    <section className="video-hero">
      <div className="video-container">
        <div className="video-placeholder">▶️ Video</div>
        <div className="video-overlay">
          <h1>{{VIDEO_HEADLINE}}</h1>
          <button className="play-button">Play</button>
        </div>
      </div>
    </section>
  )
}''',

    "VideoEmbed": '''export default function VideoEmbed() {
  return (
    <section className="video-embed">
      <div className="container">
        <h2>{{VIDEO_SECTION_HEADLINE}}</h2>
        <div className="video-wrapper">
          <div className="video-placeholder">
            🎥 Video Player
          </div>
        </div>
      </div>
    </section>
  )
}''',

    "VideoTestimonial": '''export default function VideoTestimonial() {
  const testimonials = [
    { name: '{{TESTIMONIAL_1_NAME}}', role: '{{TESTIMONIAL_1_ROLE}}', videoId: '{{VIDEO_1}}' },
    { name: '{{TESTIMONIAL_2_NAME}}', role: '{{TESTIMONIAL_2_ROLE}}', videoId: '{{VIDEO_2}}' }
  ]

  return (
    <section className="video-testimonials">
      <div className="container">
        <h2>Customer Stories</h2>
        <div className="video-testimonials-grid">
          {testimonials.map((item, i) => (
            <div key={i} className="video-testimonial-card">
              <div className="video-thumbnail">▶️</div>
              <h3>{item.name}</h3>
              <p>{item.role}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}'''
}

def generate_all_templates():
    """Generate all specialized template files"""

    categories = {
        'ecommerce': ECOMMERCE_TEMPLATES,
        'saas': SAAS_TEMPLATES,
        'restaurant': RESTAURANT_TEMPLATES,
        'cards': CARD_TEMPLATES,
        'logos': LOGO_TEMPLATES,
        'timelines': TIMELINE_TEMPLATES,
        'videos': VIDEO_TEMPLATES
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

    print(f"\n✅ Generated {total} specialized template files!")

if __name__ == "__main__":
    generate_all_templates()
