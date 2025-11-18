import { useState } from 'react'

/**
 * TransitionScale
 * Description: scale transition
 */
export default function TransitionScale({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="transitionscale" {...props}>
      <div className="transitionscale-content">
        {children}
      </div>
    </div>
  )
}