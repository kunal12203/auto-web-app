import { useState } from 'react'

/**
 * LayoutCSSGrid
 * Description: CSS grid
 */
export default function LayoutCSSGrid({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="layoutcssgrid" {...props}>
      <div className="layoutcssgrid-content">
        {children}
      </div>
    </div>
  )
}