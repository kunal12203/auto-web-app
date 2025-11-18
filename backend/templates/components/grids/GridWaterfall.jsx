import { useState } from 'react'

/**
 * GridWaterfall
 * Description: waterfall layout
 */
export default function GridWaterfall({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="gridwaterfall" {...props}>
      <div className="gridwaterfall-content">
        {children}
      </div>
    </div>
  )
}