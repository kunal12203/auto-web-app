import { useState } from 'react'

/**
 * InputMarkdown
 * Description: markdown editor
 */
export default function InputMarkdown({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputmarkdown" {...props}>
      <div className="inputmarkdown-content">
        {children}
      </div>
    </div>
  )
}