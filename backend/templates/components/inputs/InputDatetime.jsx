import { useState } from 'react'

/**
 * InputDatetime
 * Description: datetime input field
 */
export default function InputDatetime({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputdatetime" {...props}>
      <div className="inputdatetime-content">
        {children}
      </div>
    </div>
  )
}