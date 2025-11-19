import { useState } from 'react'

/**
 * ValidationAutoSave
 * Description: auto-save validation
 */
export default function ValidationAutoSave({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="validationautosave" {...props}>
      <div className="validationautosave-content">
        {children}
      </div>
    </div>
  )
}