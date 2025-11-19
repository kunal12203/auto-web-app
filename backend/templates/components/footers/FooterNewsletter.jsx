import { useState } from 'react'

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
}