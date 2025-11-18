import { useState } from 'react'

/**
 * ListNested
 * Description: nested list structure
 */
export default function ListNested({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="listnested" {...props}>
      <div className="listnested-content">
        {children}
      </div>
    </div>
  )
}