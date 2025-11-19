import { useState } from 'react'

/**
 * ValidationConditional
 * Description: conditional field validation
 */
export default function ValidationConditional({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="validationconditional" {...props}>
      <div className="validationconditional-content">
        {children}
      </div>
    </div>
  )
}