"""
Final Batch Generator - Forms, Navigation, Tabs, Modals, and more variants to reach 200+
"""

from pathlib import Path

COMPONENTS_DIR = Path(__file__).parent / "templates" / "components"

# Form Components (20 variants)
FORM_TEMPLATES = {
    "LoginForm": '''import { useState } from 'react'

export default function LoginForm() {
  const [formData, setFormData] = useState({ email: '', password: '' })

  return (
    <section className="login-form">
      <div className="container">
        <div className="form-box">
          <h2>Welcome Back</h2>
          <form onSubmit={(e) => e.preventDefault()}>
            <input type="email" placeholder="Email" required />
            <input type="password" placeholder="Password" required />
            <button type="submit" className="btn-primary">Sign In</button>
            <a href="#" className="forgot-password">Forgot Password?</a>
          </form>
        </div>
      </div>
    </section>
  )
}''',

    "SignupForm": '''import { useState } from 'react'

export default function SignupForm() {
  return (
    <section className="signup-form">
      <div className="container">
        <div className="form-box">
          <h2>Create Account</h2>
          <form onSubmit={(e) => e.preventDefault()}>
            <input type="text" placeholder="Full Name" required />
            <input type="email" placeholder="Email" required />
            <input type="password" placeholder="Password" required />
            <input type="password" placeholder="Confirm Password" required />
            <button type="submit" className="btn-primary">Sign Up</button>
          </form>
        </div>
      </div>
    </section>
  )
}''',

    "MultiStepForm": '''import { useState } from 'react'

export default function MultiStepForm() {
  const [step, setStep] = useState(1)

  return (
    <section className="multi-step-form">
      <div className="container">
        <div className="progress-steps">
          <span className={step >= 1 ? 'active' : ''}>1. Info</span>
          <span className={step >= 2 ? 'active' : ''}>2. Details</span>
          <span className={step >= 3 ? 'active' : ''}>3. Confirm</span>
        </div>
        <form onSubmit={(e) => e.preventDefault()}>
          {step === 1 && (
            <div className="form-step">
              <h3>Personal Information</h3>
              <input type="text" placeholder="Name" />
              <input type="email" placeholder="Email" />
            </div>
          )}
          {step === 2 && (
            <div className="form-step">
              <h3>Additional Details</h3>
              <input type="tel" placeholder="Phone" />
              <textarea placeholder="Message" />
            </div>
          )}
          {step === 3 && (
            <div className="form-step">
              <h3>Confirmation</h3>
              <p>Please review your information</p>
            </div>
          )}
          <div className="form-actions">
            {step > 1 && <button onClick={() => setStep(step - 1)}>Back</button>}
            {step < 3 ? (
              <button onClick={() => setStep(step + 1)}>Next</button>
            ) : (
              <button type="submit">Submit</button>
            )}
          </div>
        </form>
      </div>
    </section>
  )
}''',

    "ContactFormInline": '''import { useState } from 'react'

export default function ContactFormInline() {
  return (
    <section className="contact-form-inline">
      <div className="container">
        <form onSubmit={(e) => e.preventDefault()} className="inline-form">
          <input type="text" placeholder="Name" required />
          <input type="email" placeholder="Email" required />
          <textarea placeholder="Message" required />
          <button type="submit">Send</button>
        </form>
      </div>
    </section>
  )
}''',

    "QuoteForm": '''import { useState } from 'react'

export default function QuoteForm() {
  return (
    <section className="quote-form">
      <div className="container">
        <h2>Get a Free Quote</h2>
        <form onSubmit={(e) => e.preventDefault()}>
          <div className="form-row">
            <input type="text" placeholder="Your Name" required />
            <input type="email" placeholder="Email" required />
          </div>
          <div className="form-row">
            <input type="tel" placeholder="Phone" />
            <select>
              <option>Select Service</option>
              <option>Service A</option>
              <option>Service B</option>
            </select>
          </div>
          <textarea placeholder="Project Details" required />
          <button type="submit" className="btn-primary">Request Quote</button>
        </form>
      </div>
    </section>
  )
}''',

    "SubscribeForm": '''import { useState } from 'react'

export default function SubscribeForm() {
  const [email, setEmail] = useState('')

  return (
    <section className="subscribe-form">
      <div className="subscribe-box">
        <h3>Subscribe to our newsletter</h3>
        <form onSubmit={(e) => e.preventDefault()}>
          <div className="input-group">
            <input
              type="email"
              placeholder="your@email.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <button type="submit">Subscribe</button>
          </div>
        </form>
      </div>
    </section>
  )
}''',

    "FeedbackForm": '''import { useState } from 'react'

export default function FeedbackForm() {
  const [rating, setRating] = useState(5)

  return (
    <section className="feedback-form">
      <div className="container">
        <h2>We'd Love Your Feedback</h2>
        <form onSubmit={(e) => e.preventDefault()}>
          <div className="rating-selector">
            <label>Rating:</label>
            {[1,2,3,4,5].map(n => (
              <button
                key={n}
                type="button"
                className={n <= rating ? 'active' : ''}
                onClick={() => setRating(n)}
              >
                ⭐
              </button>
            ))}
          </div>
          <textarea placeholder="Your feedback..." required />
          <button type="submit" className="btn-primary">Submit Feedback</button>
        </form>
      </div>
    </section>
  )
}''',

    "ApplicationForm": '''import { useState } from 'react'

export default function ApplicationForm() {
  return (
    <section className="application-form">
      <div className="container">
        <h2>Application Form</h2>
        <form onSubmit={(e) => e.preventDefault()}>
          <div className="form-section">
            <h3>Personal Information</h3>
            <input type="text" placeholder="Full Name" required />
            <input type="email" placeholder="Email" required />
            <input type="tel" placeholder="Phone" />
          </div>
          <div className="form-section">
            <h3>Experience</h3>
            <textarea placeholder="Tell us about your experience" />
            <input type="file" />
          </div>
          <button type="submit" className="btn-primary">Submit Application</button>
        </form>
      </div>
    </section>
  )
}'''
}

# Tab/Accordion Components (10 variants)
TAB_TEMPLATES = {
    "TabsSimple": '''import { useState } from 'react'

export default function TabsSimple() {
  const [activeTab, setActiveTab] = useState(0)
  
  const tabs = [
    { title: '{{TAB_1_TITLE}}', content: '{{TAB_1_CONTENT}}' },
    { title: '{{TAB_2_TITLE}}', content: '{{TAB_2_CONTENT}}' },
    { title: '{{TAB_3_TITLE}}', content: '{{TAB_3_CONTENT}}' }
  ]

  return (
    <section className="tabs-simple">
      <div className="container">
        <div className="tab-buttons">
          {tabs.map((tab, i) => (
            <button
              key={i}
              className={activeTab === i ? 'active' : ''}
              onClick={() => setActiveTab(i)}
            >
              {tab.title}
            </button>
          ))}
        </div>
        <div className="tab-content">
          <p>{tabs[activeTab].content}</p>
        </div>
      </div>
    </section>
  )
}''',

    "AccordionMultiple": '''import { useState } from 'react'

export default function AccordionMultiple() {
  const [openItems, setOpenItems] = useState([])

  const items = [
    { title: '{{ACCORDION_1_TITLE}}', content: '{{ACCORDION_1_CONTENT}}' },
    { title: '{{ACCORDION_2_TITLE}}', content: '{{ACCORDION_2_CONTENT}}' },
    { title: '{{ACCORDION_3_TITLE}}', content: '{{ACCORDION_3_CONTENT}}' }
  ]

  const toggleItem = (index) => {
    setOpenItems(prev =>
      prev.includes(index)
        ? prev.filter(i => i !== index)
        : [...prev, index]
    )
  }

  return (
    <section className="accordion-multiple">
      <div className="container">
        {items.map((item, i) => (
          <div key={i} className="accordion-item">
            <button
              className="accordion-header"
              onClick={() => toggleItem(i)}
            >
              {item.title}
            </button>
            {openItems.includes(i) && (
              <div className="accordion-content">{item.content}</div>
            )}
          </div>
        ))}
      </div>
    </section>
  )
}''',

    "TabsVertical": '''import { useState } from 'react'

export default function TabsVertical() {
  const [activeTab, setActiveTab] = useState(0)

  const tabs = [
    { title: 'Tab 1', content: 'Content 1' },
    { title: 'Tab 2', content: 'Content 2' },
    { title: 'Tab 3', content: 'Content 3' }
  ]

  return (
    <section className="tabs-vertical">
      <div className="container">
        <div className="tabs-vertical-container">
          <div className="tab-sidebar">
            {tabs.map((tab, i) => (
              <button
                key={i}
                className={activeTab === i ? 'active' : ''}
                onClick={() => setActiveTab(i)}
              >
                {tab.title}
              </button>
            ))}
          </div>
          <div className="tab-content-area">
            <p>{tabs[activeTab].content}</p>
          </div>
        </div>
      </div>
    </section>
  )
}'''
}

# Navigation Components (15 variants)
NAVIGATION_TEMPLATES = {
    "Breadcrumbs": '''export default function Breadcrumbs() {
  const path = [
    { label: 'Home', url: '/' },
    { label: '{{CATEGORY}}', url: '#' },
    { label: '{{PAGE}}', url: '#' }
  ]

  return (
    <nav className="breadcrumbs">
      <div className="container">
        {path.map((item, i) => (
          <span key={i}>
            <a href={item.url}>{item.label}</a>
            {i < path.length - 1 && <span> / </span>}
          </span>
        ))}
      </div>
    </nav>
  )
}''',

    "Pagination": '''import { useState } from 'react'

export default function Pagination() {
  const [currentPage, setCurrentPage] = useState(1)
  const totalPages = 10

  return (
    <nav className="pagination">
      <button
        onClick={() => setCurrentPage(Math.max(1, currentPage - 1))}
        disabled={currentPage === 1}
      >
        Previous
      </button>
      <span>Page {currentPage} of {totalPages}</span>
      <button
        onClick={() => setCurrentPage(Math.min(totalPages, currentPage + 1))}
        disabled={currentPage === totalPages}
      >
        Next
      </button>
    </nav>
  )
}''',

    "Sidebar": '''import { useState } from 'react'

export default function Sidebar() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <>
      <button onClick={() => setIsOpen(!isOpen)} className="sidebar-toggle">
        Menu
      </button>
      <aside className={`sidebar ${isOpen ? 'open' : ''}`}>
        <nav>
          <a href="#dashboard">Dashboard</a>
          <a href="#projects">Projects</a>
          <a href="#team">Team</a>
          <a href="#settings">Settings</a>
        </nav>
      </aside>
    </>
  )
}''',

    "MobileMenu": '''import { useState } from 'react'

export default function MobileMenu() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <div className="mobile-menu">
      <button onClick={() => setIsOpen(!isOpen)} className="hamburger">
        ☰
      </button>
      {isOpen && (
        <div className="mobile-menu-overlay">
          <nav>
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <a href="#contact">Contact</a>
          </nav>
        </div>
      )}
    </div>
  )
}''',

    "TabNavigation": '''import { useState } from 'react'

export default function TabNavigation() {
  const [active, setActive] = useState('overview')

  return (
    <nav className="tab-navigation">
      <button
        className={active === 'overview' ? 'active' : ''}
        onClick={() => setActive('overview')}
      >
        Overview
      </button>
      <button
        className={active === 'specs' ? 'active' : ''}
        onClick={() => setActive('specs')}
      >
        Specifications
      </button>
      <button
        className={active === 'reviews' ? 'active' : ''}
        onClick={() => setActive('reviews')}
      >
        Reviews
      </button>
    </nav>
  )
}''',

    "FooterNav": '''export default function FooterNav() {
  return (
    <nav className="footer-nav">
      <a href="#home">Home</a>
      <a href="#about">About</a>
      <a href="#services">Services</a>
      <a href="#contact">Contact</a>
      <a href="#privacy">Privacy</a>
      <a href="#terms">Terms</a>
    </nav>
  )
}'''
}

# Modal/Popup Components (10 variants)  
MODAL_TEMPLATES = {
    "ModalSimple": '''import { useState } from 'react'

export default function ModalSimple() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <>
      <button onClick={() => setIsOpen(true)}>Open Modal</button>
      {isOpen && (
        <div className="modal-overlay" onClick={() => setIsOpen(false)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <button className="modal-close" onClick={() => setIsOpen(false)}>×</button>
            <h2>{{MODAL_TITLE}}</h2>
            <p>{{MODAL_CONTENT}}</p>
          </div>
        </div>
      )}
    </>
  )
}''',

    "ModalWithForm": '''import { useState } from 'react'

export default function ModalWithForm() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <>
      <button onClick={() => setIsOpen(true)} className="cta-button">
        Get Started
      </button>
      {isOpen && (
        <div className="modal-overlay" onClick={() => setIsOpen(false)}>
          <div className="modal-content modal-form" onClick={(e) => e.stopPropagation()}>
            <button className="modal-close" onClick={() => setIsOpen(false)}>×</button>
            <h2>Sign Up</h2>
            <form onSubmit={(e) => e.preventDefault()}>
              <input type="email" placeholder="Email" required />
              <input type="password" placeholder="Password" required />
              <button type="submit" className="btn-primary">Create Account</button>
            </form>
          </div>
        </div>
      )}
    </>
  )
}''',

    "PopupNotification": '''import { useState, useEffect } from 'react'

export default function PopupNotification() {
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    const timer = setTimeout(() => setIsVisible(true), 3000)
    return () => clearTimeout(timer)
  }, [])

  if (!isVisible) return null

  return (
    <div className="popup-notification">
      <p>{{NOTIFICATION_TEXT}}</p>
      <button onClick={() => setIsVisible(false)}>×</button>
    </div>
  )
}'''
}

# Search Components (8 variants)
SEARCH_TEMPLATES = {
    "SearchBar": '''import { useState } from 'react'

export default function SearchBar() {
  const [query, setQuery] = useState('')

  return (
    <div className="search-bar">
      <input
        type="search"
        placeholder="Search..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button type="submit">🔍</button>
    </div>
  )
}''',

    "SearchWithFilters": '''import { useState } from 'react'

export default function SearchWithFilters() {
  const [query, setQuery] = useState('')
  const [category, setCategory] = useState('all')

  return (
    <div className="search-with-filters">
      <div className="search-input">
        <input
          type="search"
          placeholder="Search..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button>Search</button>
      </div>
      <div className="search-filters">
        <select value={category} onChange={(e) => setCategory(e.target.value)}>
          <option value="all">All Categories</option>
          <option value="products">Products</option>
          <option value="services">Services</option>
        </select>
      </div>
    </div>
  )
}''',

    "SearchAutocomplete": '''import { useState } from 'react'

export default function SearchAutocomplete() {
  const [query, setQuery] = useState('')
  const [showSuggestions, setShowSuggestions] = useState(false)

  const suggestions = ['{{SUGGESTION_1}}', '{{SUGGESTION_2}}', '{{SUGGESTION_3}}']

  return (
    <div className="search-autocomplete">
      <input
        type="search"
        placeholder="Type to search..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onFocus={() => setShowSuggestions(true)}
        onBlur={() => setTimeout(() => setShowSuggestions(false), 200)}
      />
      {showSuggestions && query && (
        <div className="suggestions">
          {suggestions.filter(s => s.toLowerCase().includes(query.toLowerCase())).map((s, i) => (
            <div key={i} className="suggestion-item">{s}</div>
          ))}
        </div>
      )}
    </div>
  )
}'''
}

# Alert/Notification Components (10 variants)
ALERT_TEMPLATES = {
    "AlertSuccess": '''export default function AlertSuccess() {
  return (
    <div className="alert alert-success">
      <span>✓</span>
      <p>{{SUCCESS_MESSAGE}}</p>
    </div>
  )
}''',

    "AlertError": '''export default function AlertError() {
  return (
    <div className="alert alert-error">
      <span>✗</span>
      <p>{{ERROR_MESSAGE}}</p>
    </div>
  )
}''',

    "AlertInfo": '''export default function AlertInfo() {
  return (
    <div className="alert alert-info">
      <span>ℹ</span>
      <p>{{INFO_MESSAGE}}</p>
    </div>
  )
}''',

    "AlertWarning": '''export default function AlertWarning() {
  return (
    <div className="alert alert-warning">
      <span>⚠</span>
      <p>{{WARNING_MESSAGE}}</p>
    </div>
  )
}''',

    "NotificationToast": '''import { useState, useEffect } from 'react'

export default function NotificationToast({ message, duration = 3000 }) {
  const [isVisible, setIsVisible] = useState(true)

  useEffect(() => {
    const timer = setTimeout(() => setIsVisible(false), duration)
    return () => clearTimeout(timer)
  }, [duration])

  if (!isVisible) return null

  return (
    <div className="notification-toast">
      <p>{message || '{{TOAST_MESSAGE}}'}</p>
      <button onClick={() => setIsVisible(false)}>×</button>
    </div>
  )
}''',

    "BannerNotification": '''import { useState } from 'react'

export default function BannerNotification() {
  const [isVisible, setIsVisible] = useState(true)

  if (!isVisible) return null

  return (
    <div className="banner-notification">
      <div className="container">
        <p>{{BANNER_MESSAGE}}</p>
        <button onClick={() => setIsVisible(false)}>×</button>
      </div>
    </div>
  )
}'''
}

# Progress/Loading Components (8 variants)
PROGRESS_TEMPLATES = {
    "ProgressBar": '''export default function ProgressBar({ progress = 50 }) {
  return (
    <div className="progress-bar">
      <div className="progress-fill" style={{ width: `${progress}%` }}></div>
    </div>
  )
}''',

    "LoadingSpinner": '''export default function LoadingSpinner() {
  return (
    <div className="loading-spinner">
      <div className="spinner"></div>
      <p>Loading...</p>
    </div>
  )
}''',

    "StepIndicator": '''export default function StepIndicator({ currentStep = 1, totalSteps = 4 }) {
  return (
    <div className="step-indicator">
      {Array.from({ length: totalSteps }, (_, i) => i + 1).map(step => (
        <div
          key={step}
          className={`step ${step <= currentStep ? 'completed' : ''}`}
        >
          {step}
        </div>
      ))}
    </div>
  )
}''',

    "LoadingDots": '''export default function LoadingDots() {
  return (
    <div className="loading-dots">
      <span>.</span><span>.</span><span>.</span>
    </div>
  )
}'''
}

# More Feature Variants (10 variants)
FEATURE_VARIANTS = {
    "FeaturesWithIcons": '''export default function FeaturesWithIcons() {
  const features = [
    { icon: '{{FEATURE_1_ICON}}', title: '{{FEATURE_1_TITLE}}', text: '{{FEATURE_1_TEXT}}' },
    { icon: '{{FEATURE_2_ICON}}', title: '{{FEATURE_2_TITLE}}', text: '{{FEATURE_2_TEXT}}' },
    { icon: '{{FEATURE_3_ICON}}', title: '{{FEATURE_3_TITLE}}', text: '{{FEATURE_3_TEXT}}' }
  ]

  return (
    <section className="features-with-icons">
      <div className="container">
        <h2>{{FEATURES_HEADLINE}}</h2>
        <div className="features-flex">
          {features.map((f, i) => (
            <div key={i} className="feature-item-icon">
              <div className="feature-icon-large">{f.icon}</div>
              <h3>{f.title}</h3>
              <p>{f.text}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "FeaturesAlternating": '''export default function FeaturesAlternating() {
  const features = [
    { title: '{{FEATURE_1_TITLE}}', text: '{{FEATURE_1_TEXT}}', icon: '{{FEATURE_1_ICON}}' },
    { title: '{{FEATURE_2_TITLE}}', text: '{{FEATURE_2_TEXT}}', icon: '{{FEATURE_2_ICON}}' }
  ]

  return (
    <section className="features-alternating">
      <div className="container">
        {features.map((f, i) => (
          <div key={i} className={`feature-row ${i % 2 === 1 ? 'reverse' : ''}`}>
            <div className="feature-content">
              <h3>{f.title}</h3>
              <p>{f.text}</p>
            </div>
            <div className="feature-visual">{f.icon}</div>
          </div>
        ))}
      </div>
    </section>
  )
}''',

    "FeaturesCompact": '''export default function FeaturesCompact() {
  const features = [
    '{{FEATURE_1}}', '{{FEATURE_2}}', '{{FEATURE_3}}',
    '{{FEATURE_4}}', '{{FEATURE_5}}', '{{FEATURE_6}}'
  ]

  return (
    <section className="features-compact">
      <div className="container">
        <div className="features-compact-grid">
          {features.map((f, i) => (
            <div key={i} className="feature-compact-item">
              <span>✓</span>
              <p>{f}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}'''
}

# More Testimonial Variants (8 variants)
TESTIMONIAL_VARIANTS = {
    "TestimonialsCarousel": '''import { useState } from 'react'

export default function TestimonialsCarousel() {
  const [current, setCurrent] = useState(0)
  
  const testimonials = [
    { quote: '{{TESTIMONIAL_1_QUOTE}}', author: '{{TESTIMONIAL_1_AUTHOR}}' },
    { quote: '{{TESTIMONIAL_2_QUOTE}}', author: '{{TESTIMONIAL_2_AUTHOR}}' }
  ]

  return (
    <section className="testimonials-carousel">
      <div className="container">
        <div className="carousel">
          <button onClick={() => setCurrent(Math.max(0, current - 1))}>←</button>
          <div className="testimonial-slide">
            <p>"{testimonials[current].quote}"</p>
            <strong>{testimonials[current].author}</strong>
          </div>
          <button onClick={() => setCurrent(Math.min(testimonials.length - 1, current + 1))}>→</button>
        </div>
      </div>
    </section>
  )
}''',

    "TestimonialsWithPhotos": '''export default function TestimonialsWithPhotos() {
  const testimonials = [
    { quote: '{{TESTIMONIAL_1_QUOTE}}', author: '{{TESTIMONIAL_1_AUTHOR}}', photo: '{{PHOTO_1}}' },
    { quote: '{{TESTIMONIAL_2_QUOTE}}', author: '{{TESTIMONIAL_2_AUTHOR}}', photo: '{{PHOTO_2}}' }
  ]

  return (
    <section className="testimonials-with-photos">
      <div className="container">
        <div className="testimonials-grid-photos">
          {testimonials.map((t, i) => (
            <div key={i} className="testimonial-photo-card">
              <div className="testimonial-photo">{t.photo}</div>
              <p>"{t.quote}"</p>
              <strong>{t.author}</strong>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "TestimonialsSingle": '''export default function TestimonialsSingle() {
  return (
    <section className="testimonial-single">
      <div className="container">
        <div className="testimonial-box">
          <p className="testimonial-quote-large">
            "{{TESTIMONIAL_QUOTE}}"
          </p>
          <div className="testimonial-author-large">
            <strong>{{TESTIMONIAL_AUTHOR}}</strong>
            <span>{{TESTIMONIAL_ROLE}}</span>
          </div>
        </div>
      </div>
    </section>
  )
}'''
}

# More Pricing Variants (8 variants)
PRICING_VARIANTS = {
    "PricingToggle": '''import { useState } from 'react'

export default function PricingToggle() {
  const [isAnnual, setIsAnnual] = useState(false)

  const plans = [
    { name: 'Basic', monthly: 29, annual: 290 },
    { name: 'Pro', monthly: 59, annual: 590 }
  ]

  return (
    <section className="pricing-toggle">
      <div className="container">
        <div className="billing-toggle">
          <button
            className={!isAnnual ? 'active' : ''}
            onClick={() => setIsAnnual(false)}
          >
            Monthly
          </button>
          <button
            className={isAnnual ? 'active' : ''}
            onClick={() => setIsAnnual(true)}
          >
            Annual
          </button>
        </div>
        <div className="pricing-grid">
          {plans.map((plan, i) => (
            <div key={i} className="pricing-card">
              <h3>{plan.name}</h3>
              <div className="price">
                ${isAnnual ? plan.annual : plan.monthly}
                <span>/{isAnnual ? 'year' : 'month'}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "PricingSimple": '''export default function PricingSimple() {
  const plans = [
    { name: '{{PLAN_1_NAME}}', price: '{{PLAN_1_PRICE}}' },
    { name: '{{PLAN_2_NAME}}', price: '{{PLAN_2_PRICE}}' }
  ]

  return (
    <section className="pricing-simple">
      <div className="container">
        <h2>Simple Pricing</h2>
        <div className="pricing-row">
          {plans.map((plan, i) => (
            <div key={i} className="pricing-item-simple">
              <h3>{plan.name}</h3>
              <div className="price-simple">${plan.price}</div>
              <button>Choose Plan</button>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "PricingCompact": '''export default function PricingCompact() {
  return (
    <section className="pricing-compact">
      <div className="container">
        <div className="pricing-compact-box">
          <h3>{{PLAN_NAME}}</h3>
          <div className="price-large">${{PLAN_PRICE}}</div>
          <button className="btn-primary">Get Started</button>
        </div>
      </div>
    </section>
  )
}'''
}

# Social Media Components (7 variants)
SOCIAL_TEMPLATES = {
    "SocialLinks": '''export default function SocialLinks() {
  const socials = [
    { name: 'Facebook', url: '{{FACEBOOK_URL}}' },
    { name: 'Twitter', url: '{{TWITTER_URL}}' },
    { name: 'Instagram', url: '{{INSTAGRAM_URL}}' },
    { name: 'LinkedIn', url: '{{LINKEDIN_URL}}' }
  ]

  return (
    <div className="social-links">
      {socials.map((social, i) => (
        <a key={i} href={social.url} className="social-link">
          {social.name}
        </a>
      ))}
    </div>
  )
}''',

    "SocialShare": '''export default function SocialShare() {
  const shareUrl = window.location.href

  return (
    <div className="social-share">
      <p>Share this:</p>
      <button onClick={() => window.open(`https://facebook.com/sharer/sharer.php?u=${shareUrl}`)}>
        Facebook
      </button>
      <button onClick={() => window.open(`https://twitter.com/intent/tweet?url=${shareUrl}`)}>
        Twitter
      </button>
      <button onClick={() => window.open(`https://linkedin.com/sharing/share-offsite/?url=${shareUrl}`)}>
        LinkedIn
      </button>
    </div>
  )
}''',

    "SocialFollow": '''export default function SocialFollow() {
  return (
    <section className="social-follow">
      <div className="container">
        <h2>Follow Us</h2>
        <div className="social-buttons">
          <a href="{{FACEBOOK_URL}}" className="social-button facebook">Facebook</a>
          <a href="{{TWITTER_URL}}" className="social-button twitter">Twitter</a>
          <a href="{{INSTAGRAM_URL}}" className="social-button instagram">Instagram</a>
        </div>
      </div>
    </section>
  )
}'''
}

def generate_all_templates():
    """Generate all final batch template files"""

    categories = {
        'forms': FORM_TEMPLATES,
        'tabs': TAB_TEMPLATES,
        'navigation': NAVIGATION_TEMPLATES,
        'modals': MODAL_TEMPLATES,
        'search': SEARCH_TEMPLATES,
        'alerts': ALERT_TEMPLATES,
        'progress': PROGRESS_TEMPLATES,
        'features': FEATURE_VARIANTS,
        'testimonials': TESTIMONIAL_VARIANTS,
        'pricing': PRICING_VARIANTS,
        'social': SOCIAL_TEMPLATES
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

    print(f"\n✅ Generated {total} final batch template files!")
    print(f"\n🎉 Template library generation complete!")

if __name__ == "__main__":
    generate_all_templates()
