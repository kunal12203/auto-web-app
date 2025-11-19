import { useState } from 'react'

/**
 * InputText
 * Description: text input field
 */
export default function InputText({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputtext" {...props}>
      <div className="inputtext-content">
        {children}
      </div>
    </div>
  )
}