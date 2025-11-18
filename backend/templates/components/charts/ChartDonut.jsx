import { useState } from 'react'

/**
 * ChartDonut
 * Description: donut chart
 */
export default function ChartDonut({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="chartdonut" {...props}>
      <div className="chartdonut-content">
        {children}
      </div>
    </div>
  )
}