import { useState } from 'react'

/**
 * ProductZoomView
 * Description: product zoom view
 */
export default function ProductZoomView({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="productzoomview" {...props}>
      <div className="productzoomview-content">
        {children}
      </div>
    </div>
  )
}