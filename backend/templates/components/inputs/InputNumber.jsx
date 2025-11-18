import { useState } from 'react'

/**
 * InputNumber
 * Description: number input field
 */
export default function InputNumber({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputnumber" {...props}>
      <div className="inputnumber-content">
        {children}
      </div>
    </div>
  )
}