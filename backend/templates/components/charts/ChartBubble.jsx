import { useState } from 'react'

/**
 * ChartBubble
 * Description: bubble chart
 */
export default function ChartBubble({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="chartbubble" {...props}>
      <div className="chartbubble-content">
        {children}
      </div>
    </div>
  )
}