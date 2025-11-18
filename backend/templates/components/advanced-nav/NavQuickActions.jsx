import { useState } from 'react'

/**
 * NavQuickActions
 * Description: quick actions menu
 */
export default function NavQuickActions({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="navquickactions" {...props}>
      <div className="navquickactions-content">
        {children}
      </div>
    </div>
  )
}