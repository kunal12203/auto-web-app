import { useState } from 'react'

/**
 * OverlayVeil
 * Description: veil overlay
 */
export default function OverlayVeil({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="overlayveil" {...props}>
      <div className="overlayveil-content">
        {children}
      </div>
    </div>
  )
}