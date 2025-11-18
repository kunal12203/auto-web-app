import { useState } from 'react'

/**
 * OverlayDimmer
 * Description: dimmer overlay
 */
export default function OverlayDimmer({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="overlaydimmer" {...props}>
      <div className="overlaydimmer-content">
        {children}
      </div>
    </div>
  )
}