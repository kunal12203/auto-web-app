import { useState } from 'react'

/**
 * ContainerDockLayout
 * Description: dock layout
 */
export default function ContainerDockLayout({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="containerdocklayout" {...props}>
      <div className="containerdocklayout-content">
        {children}
      </div>
    </div>
  )
}