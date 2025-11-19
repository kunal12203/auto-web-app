import { useState } from 'react'

/**
 * MapHeatmap
 * Description: heatmap overlay
 */
export default function MapHeatmap({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="mapheatmap" {...props}>
      <div className="mapheatmap-content">
        {children}
      </div>
    </div>
  )
}