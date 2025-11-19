import { useState } from 'react'

/**
 * NotificationBadge
 * Description: badge notification
 */
export default function NotificationBadge({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="notificationbadge" {...props}>
      <div className="notificationbadge-content">
        {children}
      </div>
    </div>
  )
}