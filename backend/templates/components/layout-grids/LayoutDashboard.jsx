import { useState } from 'react'

/**
 * LayoutDashboard
 * Description: dashboard layout
 */
export default function LayoutDashboard({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="layoutdashboard" {...props}>
      <div className="layoutdashboard-content">
        {children}
      </div>
    </div>
  )
}