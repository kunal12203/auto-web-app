import { useState } from 'react'

/**
 * LoadingShimmer
 * Description: shimmer loading
 */
export default function LoadingShimmer({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="loadingshimmer" {...props}>
      <div className="loadingshimmer-content">
        {children}
      </div>
    </div>
  )
}