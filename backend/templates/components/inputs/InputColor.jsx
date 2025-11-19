import { useState } from 'react'

/**
 * InputColor
 * Description: color input field
 */
export default function InputColor({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputcolor" {...props}>
      <div className="inputcolor-content">
        {children}
      </div>
    </div>
  )
}