import { useState, useEffect } from 'react'

export default function NewsletterPopup() {
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    const timer = setTimeout(() => setIsVisible(true), 5000)
    return () => clearTimeout(timer)
  }, [])

  if (!isVisible) return null

  return (
    <div className="newsletter-popup-overlay" onClick={() => setIsVisible(false)}>
      <div className="newsletter-popup" onClick={(e) => e.stopPropagation()}>
        <button className="popup-close" onClick={() => setIsVisible(false)}>×</button>
        <h3>{{NEWSLETTER_HEADLINE}}</h3>
        <p>{{NEWSLETTER_SUBHEADLINE}}</p>
        <form onSubmit={(e) => e.preventDefault()}>
          <input type="email" placeholder="Email" required />
          <button type="submit">Subscribe</button>
        </form>
      </div>
    </div>
  )
}