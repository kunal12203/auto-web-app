import { useState } from 'react'

/**
 * PortalNotification
 * Description: notification portal
 */
export default function PortalNotification({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="portalnotification" {...props}>
      <div className="portalnotification-content">
        {children}
      </div>
    </div>
  )
}