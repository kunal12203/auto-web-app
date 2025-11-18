import { useState } from 'react'

/**
 * EditorFormula
 * Description: formula editor
 */
export default function EditorFormula({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="editorformula" {...props}>
      <div className="editorformula-content">
        {children}
      </div>
    </div>
  )
}