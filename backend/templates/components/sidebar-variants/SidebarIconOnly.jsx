import { useState } from 'react'

/**
 * SidebarIconOnly
 * Description: icon-only sidebar
 */
export default function SidebarIconOnly({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="sidebaricononly" {...props}>
      <div className="sidebaricononly-content">
        {children}
      </div>
    </div>
  )
}