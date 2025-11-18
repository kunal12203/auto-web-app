import { useState } from 'react'

/**
 * SidebarNested
 * Description: nested sidebar
 */
export default function SidebarNested({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="sidebarnested" {...props}>
      <div className="sidebarnested-content">
        {children}
      </div>
    </div>
  )
}