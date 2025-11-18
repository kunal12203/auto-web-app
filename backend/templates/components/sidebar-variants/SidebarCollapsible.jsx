import { useState } from 'react'

/**
 * SidebarCollapsible
 * Description: collapsible sidebar
 */
export default function SidebarCollapsible({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="sidebarcollapsible" {...props}>
      <div className="sidebarcollapsible-content">
        {children}
      </div>
    </div>
  )
}