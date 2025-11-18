import { useState } from 'react'

/**
 * TransitionCollapse
 * Description: collapse transition
 */
export default function TransitionCollapse({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="transitioncollapse" {...props}>
      <div className="transitioncollapse-content">
        {children}
      </div>
    </div>
  )
}