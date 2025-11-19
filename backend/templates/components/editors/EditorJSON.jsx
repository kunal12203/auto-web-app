import { useState } from 'react'

/**
 * EditorJSON
 * Description: JSON editor
 */
export default function EditorJSON({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="editorjson" {...props}>
      <div className="editorjson-content">
        {children}
      </div>
    </div>
  )
}