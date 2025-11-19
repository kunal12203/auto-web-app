import { useState } from 'react'

/**
 * SidebarMultiLevel
 * Description: multi-level sidebar
 */
export default function SidebarMultiLevel({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="sidebarmultilevel" {...props}>
      <div className="sidebarmultilevel-content">
        {children}
      </div>
    </div>
  )
}