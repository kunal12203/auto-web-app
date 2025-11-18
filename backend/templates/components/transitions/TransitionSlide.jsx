import { useState } from 'react'

/**
 * TransitionSlide
 * Description: slide transition
 */
export default function TransitionSlide({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="transitionslide" {...props}>
      <div className="transitionslide-content">
        {children}
      </div>
    </div>
  )
}