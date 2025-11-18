import { useState } from 'react'

/**
 * ImageComparison
 * Description: image comparison slider
 */
export default function ImageComparison({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="imagecomparison" {...props}>
      <div className="imagecomparison-content">
        {children}
      </div>
    </div>
  )
}