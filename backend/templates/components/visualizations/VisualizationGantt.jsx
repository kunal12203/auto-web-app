import { useState } from 'react'

/**
 * VisualizationGantt
 * Description: Gantt chart
 */
export default function VisualizationGantt({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="visualizationgantt" {...props}>
      <div className="visualizationgantt-content">
        {children}
      </div>
    </div>
  )
}