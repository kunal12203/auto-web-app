import { useState } from 'react'

/**
 * ImageSlider
 * Description: image slider
 */
export default function ImageSlider({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="imageslider" {...props}>
      <div className="imageslider-content">
        {children}
      </div>
    </div>
  )
}