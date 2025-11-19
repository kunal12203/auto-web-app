import { useState } from 'react'

/**
 * MediaAudioPlayer
 * Description: audio player
 */
export default function MediaAudioPlayer({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="mediaaudioplayer" {...props}>
      <div className="mediaaudioplayer-content">
        {children}
      </div>
    </div>
  )
}