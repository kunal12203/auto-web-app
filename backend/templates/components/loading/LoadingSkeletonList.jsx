import { useState } from 'react'

/**
 * LoadingSkeletonList
 * Description: skeleton list loader
 */
export default function LoadingSkeletonList({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="loadingskeletonlist" {...props}>
      <div className="loadingskeletonlist-content">
        {children}
      </div>
    </div>
  )
}