import { useState } from 'react'

/**
 * EditorWYSIWYG
 * Description: WYSIWYG editor
 */
export default function EditorWYSIWYG({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="editorwysiwyg" {...props}>
      <div className="editorwysiwyg-content">
        {children}
      </div>
    </div>
  )
}