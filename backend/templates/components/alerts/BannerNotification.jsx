import { useState } from 'react'

export default function BannerNotification() {
  const [isVisible, setIsVisible] = useState(true)

  if (!isVisible) return null

  return (
    <div className="banner-notification">
      <div className="container">
        <p>{{BANNER_MESSAGE}}</p>
        <button onClick={() => setIsVisible(false)}>×</button>
      </div>
    </div>
  )
}