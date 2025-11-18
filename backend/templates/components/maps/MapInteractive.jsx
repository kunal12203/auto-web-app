import { useState } from 'react'

/**
 * MapInteractive
 * Description: interactive map
 */
export default function MapInteractive({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="mapinteractive" {...props}>
      <div className="mapinteractive-content">
        {children}
      </div>
    </div>
  )
}