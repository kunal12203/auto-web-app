import { useState } from 'react'

/**
 * VisualizationNetworkGraph
 * Description: network graph
 */
export default function VisualizationNetworkGraph({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="visualizationnetworkgraph" {...props}>
      <div className="visualizationnetworkgraph-content">
        {children}
      </div>
    </div>
  )
}