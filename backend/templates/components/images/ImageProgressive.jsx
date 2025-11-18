import { useState } from 'react'

/**
 * ImageProgressive
 * Description: progressive image loading
 */
export default function ImageProgressive({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="imageprogressive" {...props}>
      <div className="imageprogressive-content">
        {children}
      </div>
    </div>
  )
}