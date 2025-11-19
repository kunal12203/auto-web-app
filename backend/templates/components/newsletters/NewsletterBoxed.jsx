import { useState } from 'react'

export default function Newsletter() {
  return (
    <section className="newsletter newsletter-boxed">
      <div className="container">
        <div className="newsletter-box">
          <div className="newsletter-icon">{{NEWSLETTER_ICON}}</div>
          <h2>{{NEWSLETTER_HEADLINE}}</h2>
          <p>{{NEWSLETTER_SUBHEADLINE}}</p>
          <form onSubmit={(e) => e.preventDefault()} className="newsletter-form">
            <input type="email" placeholder="Enter your email" required />
            <button type="submit">{{NEWSLETTER_BUTTON}}</button>
          </form>
        </div>
      </div>
    </section>
  )
}