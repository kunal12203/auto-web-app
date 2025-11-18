import { useState } from 'react'

export default function Hero() {
  const [email, setEmail] = useState('')

  return (
    <section className="hero hero-with-form" id="home">
      <div className="container">
        <h1>{{HERO_HEADLINE}}</h1>
        <p>{{HERO_SUBHEADLINE}}</p>
        <form onSubmit={(e) => e.preventDefault()} className="hero-form">
          <input
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <button type="submit">{{CTA_PRIMARY}}</button>
        </form>
        <p className="hero-note">{{HERO_NOTE}}</p>
      </div>
    </section>
  )
}