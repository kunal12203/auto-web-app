import { useState } from 'react'

/**
 * OverlayMask
 * Description: mask overlay
 */
export default function OverlayMask({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="overlaymask" {...props}>
      <div className="overlaymask-content">
        {children}
      </div>
    </div>
  )
}