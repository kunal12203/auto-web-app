import { useState } from 'react'

/**
 * LoadingProgressive
 * Description: progressive loading
 */
export default function LoadingProgressive({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="loadingprogressive" {...props}>
      <div className="loadingprogressive-content">
        {children}
      </div>
    </div>
  )
}