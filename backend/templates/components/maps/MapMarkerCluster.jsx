import { useState } from 'react'

/**
 * MapMarkerCluster
 * Description: marker clustering map
 */
export default function MapMarkerCluster({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="mapmarkercluster" {...props}>
      <div className="mapmarkercluster-content">
        {children}
      </div>
    </div>
  )
}