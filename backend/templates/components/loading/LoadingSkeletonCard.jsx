import { useState } from 'react'

/**
 * LoadingSkeletonCard
 * Description: skeleton card loader
 */
export default function LoadingSkeletonCard({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="loadingskeletoncard" {...props}>
      <div className="loadingskeletoncard-content">
        {children}
      </div>
    </div>
  )
}