import { useState } from 'react'

/**
 * ValidationFieldArray
 * Description: dynamic field array validation
 */
export default function ValidationFieldArray({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="validationfieldarray" {...props}>
      <div className="validationfieldarray-content">
        {children}
      </div>
    </div>
  )
}