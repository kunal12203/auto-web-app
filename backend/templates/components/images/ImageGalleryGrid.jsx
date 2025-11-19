import { useState } from 'react'

/**
 * ImageGalleryGrid
 * Description: image gallery grid
 */
export default function ImageGalleryGrid({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="imagegallerygrid" {...props}>
      <div className="imagegallerygrid-content">
        {children}
      </div>
    </div>
  )
}