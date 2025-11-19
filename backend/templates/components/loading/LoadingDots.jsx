import { useState } from 'react'

/**
 * LoadingDots
 * Description: dots loader
 */
export default function LoadingDots({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="loadingdots" {...props}>
      <div className="loadingdots-content">
        {children}
      </div>
    </div>
  )
}