import { useState } from 'react'

/**
 * TransitionRotate
 * Description: rotate transition
 */
export default function TransitionRotate({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="transitionrotate" {...props}>
      <div className="transitionrotate-content">
        {children}
      </div>
    </div>
  )
}