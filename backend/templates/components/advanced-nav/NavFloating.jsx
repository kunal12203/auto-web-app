import { useState } from 'react'

/**
 * NavFloating
 * Description: floating navigation
 */
export default function NavFloating({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="navfloating" {...props}>
      <div className="navfloating-content">
        {children}
      </div>
    </div>
  )
}