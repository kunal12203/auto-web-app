import { useState } from 'react'

/**
 * SidebarResponsive
 * Description: responsive sidebar
 */
export default function SidebarResponsive({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="sidebarresponsive" {...props}>
      <div className="sidebarresponsive-content">
        {children}
      </div>
    </div>
  )
}