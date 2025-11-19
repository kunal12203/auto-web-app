import { useState } from 'react'

/**
 * InputDate
 * Description: date input field
 */
export default function InputDate({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputdate" {...props}>
      <div className="inputdate-content">
        {children}
      </div>
    </div>
  )
}