import { useState } from 'react'

/**
 * MapGeofencing
 * Description: geofencing map
 */
export default function MapGeofencing({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="mapgeofencing" {...props}>
      <div className="mapgeofencing-content">
        {children}
      </div>
    </div>
  )
}