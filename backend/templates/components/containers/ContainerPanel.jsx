import { useState } from 'react'

/**
 * ContainerPanel
 * Description: panel container
 */
export default function ContainerPanel({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="containerpanel" {...props}>
      <div className="containerpanel-content">
        {children}
      </div>
    </div>
  )
}