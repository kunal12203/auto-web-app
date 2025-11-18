import { useState } from 'react'

/**
 * LoadingWave
 * Description: wave loading
 */
export default function LoadingWave({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="loadingwave" {...props}>
      <div className="loadingwave-content">
        {children}
      </div>
    </div>
  )
}