import { useState } from 'react'

/**
 * TransitionFade
 * Description: fade transition
 */
export default function TransitionFade({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="transitionfade" {...props}>
      <div className="transitionfade-content">
        {children}
      </div>
    </div>
  )
}