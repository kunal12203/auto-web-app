import { useState } from 'react'

/**
 * ChartGauge
 * Description: gauge chart
 */
export default function ChartGauge({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="chartgauge" {...props}>
      <div className="chartgauge-content">
        {children}
      </div>
    </div>
  )
}