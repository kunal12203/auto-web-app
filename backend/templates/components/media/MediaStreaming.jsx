import { useState } from 'react'

/**
 * MediaStreaming
 * Description: live streaming player
 */
export default function MediaStreaming({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="mediastreaming" {...props}>
      <div className="mediastreaming-content">
        {children}
      </div>
    </div>
  )
}