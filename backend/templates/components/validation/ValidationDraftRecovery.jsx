import { useState } from 'react'

/**
 * ValidationDraftRecovery
 * Description: draft recovery
 */
export default function ValidationDraftRecovery({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="validationdraftrecovery" {...props}>
      <div className="validationdraftrecovery-content">
        {children}
      </div>
    </div>
  )
}