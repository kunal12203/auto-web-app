import { useState } from 'react'

/**
 * ValidationInline
 * Description: inline field validation
 */
export default function ValidationInline({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="validationinline" {...props}>
      <div className="validationinline-content">
        {children}
      </div>
    </div>
  )
}