import { useState } from 'react'

/**
 * InputCodeEditor
 * Description: code editor input
 */
export default function InputCodeEditor({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputcodeeditor" {...props}>
      <div className="inputcodeeditor-content">
        {children}
      </div>
    </div>
  )
}