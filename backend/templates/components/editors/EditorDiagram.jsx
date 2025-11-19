import { useState } from 'react'

/**
 * EditorDiagram
 * Description: diagram editor
 */
export default function EditorDiagram({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="editordiagram" {...props}>
      <div className="editordiagram-content">
        {children}
      </div>
    </div>
  )
}