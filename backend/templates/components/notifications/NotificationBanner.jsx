import { useState } from 'react'

/**
 * NotificationBanner
 * Description: banner notification
 */
export default function NotificationBanner({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="notificationbanner" {...props}>
      <div className="notificationbanner-content">
        {children}
      </div>
    </div>
  )
}