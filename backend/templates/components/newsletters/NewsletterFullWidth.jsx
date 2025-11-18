import { useState } from 'react'

export default function NewsletterFullWidth() {
  return (
    <section className="newsletter-full-width">
      <div className="newsletter-full-container">
        <div className="container">
          <h2>{{NEWSLETTER_HEADLINE}}</h2>
          <p>{{NEWSLETTER_SUBHEADLINE}}</p>
          <form onSubmit={(e) => e.preventDefault()} className="newsletter-form-wide">
            <input type="email" placeholder="Enter your email" required />
            <button type="submit">Subscribe</button>
          </form>
        </div>
      </div>
    </section>
  )
}