import { useState } from 'react'

/**
 * ChartBar
 * Description: bar chart
 */
export default function ChartBar({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="chartbar" {...props}>
      <div className="chartbar-content">
        {children}
      </div>
    </div>
  )
}