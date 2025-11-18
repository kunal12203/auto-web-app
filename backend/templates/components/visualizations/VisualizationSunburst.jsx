import { useState } from 'react'

/**
 * VisualizationSunburst
 * Description: sunburst chart
 */
export default function VisualizationSunburst({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="visualizationsunburst" {...props}>
      <div className="visualizationsunburst-content">
        {children}
      </div>
    </div>
  )
}