import { useState } from 'react'

/**
 * NotificationCenter
 * Description: notification center
 */
export default function NotificationCenter({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="notificationcenter" {...props}>
      <div className="notificationcenter-content">
        {children}
      </div>
    </div>
  )
}