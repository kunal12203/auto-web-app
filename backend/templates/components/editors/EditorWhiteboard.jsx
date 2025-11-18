import { useState } from 'react'

/**
 * EditorWhiteboard
 * Description: whiteboard editor
 */
export default function EditorWhiteboard({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="editorwhiteboard" {...props}>
      <div className="editorwhiteboard-content">
        {children}
      </div>
    </div>
  )
}