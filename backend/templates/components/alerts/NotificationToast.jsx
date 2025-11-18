import { useState, useEffect } from 'react'

export default function NotificationToast({ message, duration = 3000 }) {
  const [isVisible, setIsVisible] = useState(true)

  useEffect(() => {
    const timer = setTimeout(() => setIsVisible(false), duration)
    return () => clearTimeout(timer)
  }, [duration])

  if (!isVisible) return null

  return (
    <div className="notification-toast">
      <p>{message || '{{TOAST_MESSAGE}}'}</p>
      <button onClick={() => setIsVisible(false)}>×</button>
    </div>
  )
}