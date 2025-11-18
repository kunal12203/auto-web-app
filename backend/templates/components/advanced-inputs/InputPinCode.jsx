import { useState } from 'react'

/**
 * InputPinCode
 * Description: PIN code input
 */
export default function InputPinCode({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputpincode" {...props}>
      <div className="inputpincode-content">
        {children}
      </div>
    </div>
  )
}