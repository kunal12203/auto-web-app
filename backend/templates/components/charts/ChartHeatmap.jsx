import { useState } from 'react'

/**
 * ChartHeatmap
 * Description: heatmap chart
 */
export default function ChartHeatmap({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="chartheatmap" {...props}>
      <div className="chartheatmap-content">
        {children}
      </div>
    </div>
  )
}