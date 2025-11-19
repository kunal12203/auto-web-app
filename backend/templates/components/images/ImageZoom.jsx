import { useState } from 'react'

/**
 * ImageZoom
 * Description: zoomable image
 */
export default function ImageZoom({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="imagezoom" {...props}>
      <div className="imagezoom-content">
        {children}
      </div>
    </div>
  )
}