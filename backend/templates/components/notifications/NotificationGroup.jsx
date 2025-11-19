import { useState } from 'react'

/**
 * NotificationGroup
 * Description: grouped notifications
 */
export default function NotificationGroup({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="notificationgroup" {...props}>
      <div className="notificationgroup-content">
        {children}
      </div>
    </div>
  )
}