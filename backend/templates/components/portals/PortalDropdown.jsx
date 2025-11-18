import { useState } from 'react'

/**
 * PortalDropdown
 * Description: dropdown portal
 */
export default function PortalDropdown({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="portaldropdown" {...props}>
      <div className="portaldropdown-content">
        {children}
      </div>
    </div>
  )
}