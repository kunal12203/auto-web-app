import { useState } from 'react'

/**
 * NotificationFloating
 * Description: floating notification
 */
export default function NotificationFloating({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="notificationfloating" {...props}>
      <div className="notificationfloating-content">
        {children}
      </div>
    </div>
  )
}