import { useState } from 'react'

/**
 * NotificationPriority
 * Description: priority queue notifications
 */
export default function NotificationPriority({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="notificationpriority" {...props}>
      <div className="notificationpriority-content">
        {children}
      </div>
    </div>
  )
}