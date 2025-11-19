import { useState } from 'react'

/**
 * SidebarFilterable
 * Description: filterable sidebar
 */
export default function SidebarFilterable({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="sidebarfilterable" {...props}>
      <div className="sidebarfilterable-content">
        {children}
      </div>
    </div>
  )
}