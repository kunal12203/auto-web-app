import { useState } from 'react'

/**
 * SidebarExpandable
 * Description: expandable sidebar
 */
export default function SidebarExpandable({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="sidebarexpandable" {...props}>
      <div className="sidebarexpandable-content">
        {children}
      </div>
    </div>
  )
}