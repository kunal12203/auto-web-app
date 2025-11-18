import { useState } from 'react'

export default function CookieBanner() {
  const [isVisible, setIsVisible] = useState(true)

  if (!isVisible) return null

  return (
    <div className="cookie-banner">
      <p>We use cookies to improve your experience. {{COOKIE_TEXT}}</p>
      <div className="cookie-actions">
        <button onClick={() => setIsVisible(false)}>Accept</button>
        <button onClick={() => setIsVisible(false)}>Decline</button>
      </div>
    </div>
  )
}