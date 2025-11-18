import { useState } from 'react'

/**
 * ChartLine
 * Description: line chart
 */
export default function ChartLine({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="chartline" {...props}>
      <div className="chartline-content">
        {children}
      </div>
    </div>
  )
}