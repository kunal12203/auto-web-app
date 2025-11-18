import { useState } from 'react'

/**
 * GridResponsive
 * Description: responsive grid system
 */
export default function GridResponsive({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="gridresponsive" {...props}>
      <div className="gridresponsive-content">
        {children}
      </div>
    </div>
  )
}