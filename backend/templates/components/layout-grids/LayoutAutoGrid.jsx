import { useState } from 'react'

/**
 * LayoutAutoGrid
 * Description: auto grid
 */
export default function LayoutAutoGrid({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="layoutautogrid" {...props}>
      <div className="layoutautogrid-content">
        {children}
      </div>
    </div>
  )
}