import { useState } from 'react'

/**
 * PortalTooltip
 * Description: tooltip portal
 */
export default function PortalTooltip({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="portaltooltip" {...props}>
      <div className="portaltooltip-content">
        {children}
      </div>
    </div>
  )
}