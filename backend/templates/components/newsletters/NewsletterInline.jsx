import { useState } from 'react'

export default function Newsletter() {
  return (
    <section className="newsletter newsletter-inline">
      <div className="container">
        <div className="newsletter-inline-content">
          <div className="newsletter-text">
            <h3>{{NEWSLETTER_HEADLINE}}</h3>
            <p>{{NEWSLETTER_SUBHEADLINE}}</p>
          </div>
          <form onSubmit={(e) => e.preventDefault()} className="newsletter-form-inline">
            <input type="email" placeholder="Your email" required />
            <button type="submit">{{NEWSLETTER_BUTTON}}</button>
          </form>
        </div>
      </div>
    </section>
  )
}