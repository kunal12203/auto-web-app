import { useState } from 'react'

/**
 * PortalModal
 * Description: modal portal
 */
export default function PortalModal({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="portalmodal" {...props}>
      <div className="portalmodal-content">
        {children}
      </div>
    </div>
  )
}