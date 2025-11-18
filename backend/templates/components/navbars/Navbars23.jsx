import { useState, useEffect } from 'react'

/**
 * Navbars23
 */
export default function Navbars23({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars23" {...props}>
      {children}
    </div>
  )
}