import { useState } from 'react'

/**
 * ImageCropper
 * Description: image cropper
 */
export default function ImageCropper({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="imagecropper" {...props}>
      <div className="imagecropper-content">
        {children}
      </div>
    </div>
  )
}