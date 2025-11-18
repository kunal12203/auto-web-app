import { useState } from 'react'

/**
 * VisualizationMindMap
 * Description: mind map
 */
export default function VisualizationMindMap({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="visualizationmindmap" {...props}>
      <div className="visualizationmindmap-content">
        {children}
      </div>
    </div>
  )
}