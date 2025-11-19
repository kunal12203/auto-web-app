import { useState } from 'react'

/**
 * NavAnchor
 * Description: anchor navigation
 */
export default function NavAnchor({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="navanchor" {...props}>
      <div className="navanchor-content">
        {children}
      </div>
    </div>
  )
}