import { useState } from 'react'

/**
 * EditorMarkdown
 * Description: Markdown editor
 */
export default function EditorMarkdown({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="editormarkdown" {...props}>
      <div className="editormarkdown-content">
        {children}
      </div>
    </div>
  )
}