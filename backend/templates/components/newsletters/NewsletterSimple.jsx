import { useState } from 'react'

export default function Newsletter() {
  const [email, setEmail] = useState('')

  return (
    <section className="newsletter newsletter-simple">
      <div className="container">
        <h2>{{NEWSLETTER_HEADLINE}}</h2>
        <p>{{NEWSLETTER_SUBHEADLINE}}</p>
        <form onSubmit={(e) => e.preventDefault()} className="newsletter-form">
          <input
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <button type="submit">{{NEWSLETTER_BUTTON}}</button>
        </form>
      </div>
    </section>
  )
}