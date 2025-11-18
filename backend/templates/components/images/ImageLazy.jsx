import { useState } from 'react'

/**
 * ImageLazy
 * Description: lazy loading image
 */
export default function ImageLazy({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="imagelazy" {...props}>
      <div className="imagelazy-content">
        {children}
      </div>
    </div>
  )
}