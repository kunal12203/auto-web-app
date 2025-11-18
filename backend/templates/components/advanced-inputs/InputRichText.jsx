import { useState } from 'react'

/**
 * InputRichText
 * Description: rich text editor input
 */
export default function InputRichText({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputrichtext" {...props}>
      <div className="inputrichtext-content">
        {children}
      </div>
    </div>
  )
}