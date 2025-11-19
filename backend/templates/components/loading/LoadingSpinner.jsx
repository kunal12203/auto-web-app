import { useState } from 'react'

/**
 * LoadingSpinner
 * Description: spinner loader
 */
export default function LoadingSpinner({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="loadingspinner" {...props}>
      <div className="loadingspinner-content">
        {children}
      </div>
    </div>
  )
}