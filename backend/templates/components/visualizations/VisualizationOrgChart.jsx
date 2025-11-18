import { useState } from 'react'

/**
 * VisualizationOrgChart
 * Description: organization chart
 */
export default function VisualizationOrgChart({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="visualizationorgchart" {...props}>
      <div className="visualizationorgchart-content">
        {children}
      </div>
    </div>
  )
}