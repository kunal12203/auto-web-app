import { useState } from 'react'

/**
 * ValidationAsync
 * Description: async validation
 */
export default function ValidationAsync({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="validationasync" {...props}>
      <div className="validationasync-content">
        {children}
      </div>
    </div>
  )
}