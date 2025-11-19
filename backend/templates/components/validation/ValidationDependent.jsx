import { useState } from 'react'

/**
 * ValidationDependent
 * Description: dependent field validation
 */
export default function ValidationDependent({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="validationdependent" {...props}>
      <div className="validationdependent-content">
        {children}
      </div>
    </div>
  )
}