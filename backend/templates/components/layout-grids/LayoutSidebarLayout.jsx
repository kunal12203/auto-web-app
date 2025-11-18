import { useState } from 'react'

/**
 * LayoutSidebarLayout
 * Description: sidebar layout
 */
export default function LayoutSidebarLayout({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="layoutsidebarlayout" {...props}>
      <div className="layoutsidebarlayout-content">
        {children}
      </div>
    </div>
  )
}