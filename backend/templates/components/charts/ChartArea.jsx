import { useState } from 'react'

/**
 * ChartArea
 * Description: area chart
 */
export default function ChartArea({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="chartarea" {...props}>
      <div className="chartarea-content">
        {children}
      </div>
    </div>
  )
}