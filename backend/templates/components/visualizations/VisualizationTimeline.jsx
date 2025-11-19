import { useState } from 'react'

/**
 * VisualizationTimeline
 * Description: timeline visualization
 */
export default function VisualizationTimeline({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="visualizationtimeline" {...props}>
      <div className="visualizationtimeline-content">
        {children}
      </div>
    </div>
  )
}