import { useState } from 'react'

/**
 * LayoutFlexGrid
 * Description: flexbox grid
 */
export default function LayoutFlexGrid({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="layoutflexgrid" {...props}>
      <div className="layoutflexgrid-content">
        {children}
      </div>
    </div>
  )
}