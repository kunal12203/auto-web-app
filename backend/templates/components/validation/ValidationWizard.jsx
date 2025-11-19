import { useState } from 'react'

/**
 * ValidationWizard
 * Description: form wizard with validation
 */
export default function ValidationWizard({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="validationwizard" {...props}>
      <div className="validationwizard-content">
        {children}
      </div>
    </div>
  )
}