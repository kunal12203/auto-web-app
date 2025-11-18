import { useState } from 'react'

export default function NewsletterWithBenefits() {
  return (
    <section className="newsletter-with-benefits">
      <div className="container">
        <div className="newsletter-content">
          <h2>{{NEWSLETTER_HEADLINE}}</h2>
          <ul className="newsletter-benefits">
            <li>✓ {{BENEFIT_1}}</li>
            <li>✓ {{BENEFIT_2}}</li>
            <li>✓ {{BENEFIT_3}}</li>
          </ul>
          <form onSubmit={(e) => e.preventDefault()}>
            <input type="email" placeholder="Email" required />
            <button type="submit">Subscribe</button>
          </form>
        </div>
      </div>
    </section>
  )
}