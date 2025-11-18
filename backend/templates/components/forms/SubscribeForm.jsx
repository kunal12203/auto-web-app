import { useState } from 'react'

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
}