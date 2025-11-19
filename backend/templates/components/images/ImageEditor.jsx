import { useState } from 'react'

/**
 * ImageEditor
 * Description: image editor
 */
export default function ImageEditor({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="imageeditor" {...props}>
      <div className="imageeditor-content">
        {children}
      </div>
    </div>
  )
}