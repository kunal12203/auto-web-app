import { useState } from 'react'

/**
 * SidebarSearchable
 * Description: searchable sidebar
 */
export default function SidebarSearchable({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="sidebarsearchable" {...props}>
      <div className="sidebarsearchable-content">
        {children}
      </div>
    </div>
  )
}