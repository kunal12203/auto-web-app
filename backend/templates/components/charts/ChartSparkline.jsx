import { useState } from 'react'

/**
 * ChartSparkline
 * Description: sparkline chart
 */
export default function ChartSparkline({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="chartsparkline" {...props}>
      <div className="chartsparkline-content">
        {children}
      </div>
    </div>
  )
}