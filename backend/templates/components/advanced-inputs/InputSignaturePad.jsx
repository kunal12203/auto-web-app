import { useState } from 'react'

/**
 * InputSignaturePad
 * Description: signature pad
 */
export default function InputSignaturePad({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputsignaturepad" {...props}>
      <div className="inputsignaturepad-content">
        {children}
      </div>
    </div>
  )
}