import { useState } from 'react'

/**
 * InputEmail
 * Description: email input field
 */
export default function InputEmail({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputemail" {...props}>
      <div className="inputemail-content">
        {children}
      </div>
    </div>
  )
}