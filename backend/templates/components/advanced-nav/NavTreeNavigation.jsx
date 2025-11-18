import { useState } from 'react'

/**
 * NavTreeNavigation
 * Description: tree navigation
 */
export default function NavTreeNavigation({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="navtreenavigation" {...props}>
      <div className="navtreenavigation-content">
        {children}
      </div>
    </div>
  )
}