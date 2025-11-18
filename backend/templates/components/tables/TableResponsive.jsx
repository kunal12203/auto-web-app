import { useState } from 'react'

/**
 * TableResponsive
 * Description: responsive table with mobile view
 */
export default function TableResponsive({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tableresponsive" {...props}>
      <div className="tableresponsive-content">
        {children}
      </div>
    </div>
  )
}