import { useState } from 'react'

/**
 * NotificationToast
 * Description: toast notification
 */
export default function NotificationToast({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="notificationtoast" {...props}>
      <div className="notificationtoast-content">
        {children}
      </div>
    </div>
  )
}