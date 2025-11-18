import { useState } from 'react'

/**
 * InputTel
 * Description: telephone input field
 */
export default function InputTel({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputtel" {...props}>
      <div className="inputtel-content">
        {children}
      </div>
    </div>
  )
}