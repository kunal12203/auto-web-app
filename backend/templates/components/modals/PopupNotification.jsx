import { useState, useEffect } from 'react'

export default function PopupNotification() {
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    const timer = setTimeout(() => setIsVisible(true), 3000)
    return () => clearTimeout(timer)
  }, [])

  if (!isVisible) return null

  return (
    <div className="popup-notification">
      <p>{{NOTIFICATION_TEXT}}</p>
      <button onClick={() => setIsVisible(false)}>×</button>
    </div>
  )
}