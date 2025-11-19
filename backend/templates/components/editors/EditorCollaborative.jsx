import { useState } from 'react'

/**
 * EditorCollaborative
 * Description: collaborative editor
 */
export default function EditorCollaborative({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="editorcollaborative" {...props}>
      <div className="editorcollaborative-content">
        {children}
      </div>
    </div>
  )
}