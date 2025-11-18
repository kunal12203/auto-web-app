import { useState } from 'react'

/**
 * NotificationInlineAlert
 * Description: inline alert
 */
export default function NotificationInlineAlert({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="notificationinlinealert" {...props}>
      <div className="notificationinlinealert-content">
        {children}
      </div>
    </div>
  )
}