import { useState } from 'react'

/**
 * MediaVideoPlayer
 * Description: video player
 */
export default function MediaVideoPlayer({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="mediavideoplayer" {...props}>
      <div className="mediavideoplayer-content">
        {children}
      </div>
    </div>
  )
}