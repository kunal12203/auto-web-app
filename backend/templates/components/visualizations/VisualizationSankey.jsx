import { useState } from 'react'

/**
 * VisualizationSankey
 * Description: Sankey diagram
 */
export default function VisualizationSankey({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="visualizationsankey" {...props}>
      <div className="visualizationsankey-content">
        {children}
      </div>
    </div>
  )
}