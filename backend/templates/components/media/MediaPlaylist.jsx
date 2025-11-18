import { useState } from 'react'

/**
 * MediaPlaylist
 * Description: media playlist
 */
export default function MediaPlaylist({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="mediaplaylist" {...props}>
      <div className="mediaplaylist-content">
        {children}
      </div>
    </div>
  )
}