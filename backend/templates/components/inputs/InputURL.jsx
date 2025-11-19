import { useState } from 'react'

/**
 * InputURL
 * Description: URL input field
 */
export default function InputURL({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputurl" {...props}>
      <div className="inputurl-content">
        {children}
      </div>
    </div>
  )
}