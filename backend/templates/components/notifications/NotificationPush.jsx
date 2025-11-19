import { useState } from 'react'

/**
 * NotificationPush
 * Description: push notification
 */
export default function NotificationPush({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="notificationpush" {...props}>
      <div className="notificationpush-content">
        {children}
      </div>
    </div>
  )
}