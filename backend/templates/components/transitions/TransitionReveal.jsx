import { useState } from 'react'

/**
 * TransitionReveal
 * Description: reveal transition
 */
export default function TransitionReveal({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="transitionreveal" {...props}>
      <div className="transitionreveal-content">
        {children}
      </div>
    </div>
  )
}