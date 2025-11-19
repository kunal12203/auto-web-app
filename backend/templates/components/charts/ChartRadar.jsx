import { useState } from 'react'

/**
 * ChartRadar
 * Description: radar chart
 */
export default function ChartRadar({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="chartradar" {...props}>
      <div className="chartradar-content">
        {children}
      </div>
    </div>
  )
}