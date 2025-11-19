import { useState } from 'react'

/**
 * ImageLightbox
 * Description: image lightbox viewer
 */
export default function ImageLightbox({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="imagelightbox" {...props}>
      <div className="imagelightbox-content">
        {children}
      </div>
    </div>
  )
}