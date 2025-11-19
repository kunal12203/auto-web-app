import { useState } from 'react'

/**
 * PortalMenu
 * Description: menu portal
 */
export default function PortalMenu({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="portalmenu" {...props}>
      <div className="portalmenu-content">
        {children}
      </div>
    </div>
  )
}