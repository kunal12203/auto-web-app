import { useState } from 'react'

/**
 * LoadingContentLoader
 * Description: content loader
 */
export default function LoadingContentLoader({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="loadingcontentloader" {...props}>
      <div className="loadingcontentloader-content">
        {children}
      </div>
    </div>
  )
}