import { useState } from 'react'

/**
 * ChartScatter
 * Description: scatter plot
 */
export default function ChartScatter({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="chartscatter" {...props}>
      <div className="chartscatter-content">
        {children}
      </div>
    </div>
  )
}