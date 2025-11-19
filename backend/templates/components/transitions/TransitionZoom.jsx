import { useState } from 'react'

/**
 * TransitionZoom
 * Description: zoom transition
 */
export default function TransitionZoom({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="transitionzoom" {...props}>
      <div className="transitionzoom-content">
        {children}
      </div>
    </div>
  )
}