import { useState } from 'react'

/**
 * InputTime
 * Description: time input field
 */
export default function InputTime({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputtime" {...props}>
      <div className="inputtime-content">
        {children}
      </div>
    </div>
  )
}