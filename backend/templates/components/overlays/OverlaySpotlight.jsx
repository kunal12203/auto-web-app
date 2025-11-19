import { useState } from 'react'

/**
 * OverlaySpotlight
 * Description: spotlight overlay
 */
export default function OverlaySpotlight({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="overlayspotlight" {...props}>
      <div className="overlayspotlight-content">
        {children}
      </div>
    </div>
  )
}