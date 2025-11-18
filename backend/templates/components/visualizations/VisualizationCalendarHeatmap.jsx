import { useState } from 'react'

/**
 * VisualizationCalendarHeatmap
 * Description: calendar heatmap
 */
export default function VisualizationCalendarHeatmap({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="visualizationcalendarheatmap" {...props}>
      <div className="visualizationcalendarheatmap-content">
        {children}
      </div>
    </div>
  )
}