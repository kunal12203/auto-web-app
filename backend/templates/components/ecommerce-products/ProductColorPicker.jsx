import { useState } from 'react'

/**
 * ProductColorPicker
 * Description: color picker
 */
export default function ProductColorPicker({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="productcolorpicker" {...props}>
      <div className="productcolorpicker-content">
        {children}
      </div>
    </div>
  )
}