import { useState } from 'react'

/**
 * ChartTreemap
 * Description: treemap chart
 */
export default function ChartTreemap({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="charttreemap" {...props}>
      <div className="charttreemap-content">
        {children}
      </div>
    </div>
  )
}