import { useState } from 'react'

/**
 * TransitionFlip
 * Description: flip transition
 */
export default function TransitionFlip({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="transitionflip" {...props}>
      <div className="transitionflip-content">
        {children}
      </div>
    </div>
  )
}