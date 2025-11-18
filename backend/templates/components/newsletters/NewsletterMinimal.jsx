import { useState } from 'react'

export default function NewsletterMinimal() {
  return (
    <section className="newsletter-minimal-section">
      <div className="container">
        <form onSubmit={(e) => e.preventDefault()} className="newsletter-minimal-form">
          <input type="email" placeholder="Subscribe to newsletter" required />
          <button type="submit">→</button>
        </form>
      </div>
    </section>
  )
}