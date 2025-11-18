import { useState } from 'react'

/**
 * InputPassword
 * Description: password input field
 */
export default function InputPassword({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputpassword" {...props}>
      <div className="inputpassword-content">
        {children}
      </div>
    </div>
  )
}