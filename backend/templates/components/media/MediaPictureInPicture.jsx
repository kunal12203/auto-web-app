import { useState } from 'react'

/**
 * MediaPictureInPicture
 * Description: picture-in-picture mode
 */
export default function MediaPictureInPicture({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="mediapictureinpicture" {...props}>
      <div className="mediapictureinpicture-content">
        {children}
      </div>
    </div>
  )
}