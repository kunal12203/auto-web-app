import { useState } from 'react'

/**
 * PortalOverlay
 * Description: overlay portal
 */
export default function PortalOverlay({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="portaloverlay" {...props}>
      <div className="portaloverlay-content">
        {children}
      </div>
    </div>
  )
}