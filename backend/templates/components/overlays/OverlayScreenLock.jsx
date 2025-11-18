import { useState } from 'react'

/**
 * OverlayScreenLock
 * Description: screen lock overlay
 */
export default function OverlayScreenLock({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="overlayscreenlock" {...props}>
      <div className="overlayscreenlock-content">
        {children}
      </div>
    </div>
  )
}