import { useState } from 'react'

/**
 * EditorCode
 * Description: code editor
 */
export default function EditorCode({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="editorcode" {...props}>
      <div className="editorcode-content">
        {children}
      </div>
    </div>
  )
}