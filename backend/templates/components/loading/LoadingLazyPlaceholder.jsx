import { useState } from 'react'

/**
 * LoadingLazyPlaceholder
 * Description: lazy placeholder
 */
export default function LoadingLazyPlaceholder({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="loadinglazyplaceholder" {...props}>
      <div className="loadinglazyplaceholder-content">
        {children}
      </div>
    </div>
  )
}