import { useState } from 'react'

/**
 * LayoutResponsiveGrid
 * Description: responsive grid
 */
export default function LayoutResponsiveGrid({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="layoutresponsivegrid" {...props}>
      <div className="layoutresponsivegrid-content">
        {children}
      </div>
    </div>
  )
}