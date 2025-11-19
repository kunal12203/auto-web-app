import { useState } from 'react'

/**
 * OverlayBackdrop
 * Description: backdrop overlay
 */
export default function OverlayBackdrop({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="overlaybackdrop" {...props}>
      <div className="overlaybackdrop-content">
        {children}
      </div>
    </div>
  )
}