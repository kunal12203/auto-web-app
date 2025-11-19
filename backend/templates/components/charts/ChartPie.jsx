import { useState } from 'react'

/**
 * ChartPie
 * Description: pie chart
 */
export default function ChartPie({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="chartpie" {...props}>
      <div className="chartpie-content">
        {children}
      </div>
    </div>
  )
}