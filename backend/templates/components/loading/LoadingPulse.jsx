import { useState } from 'react'

/**
 * LoadingPulse
 * Description: pulse loading
 */
export default function LoadingPulse({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="loadingpulse" {...props}>
      <div className="loadingpulse-content">
        {children}
      </div>
    </div>
  )
}