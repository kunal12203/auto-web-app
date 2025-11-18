import { useState, useEffect } from 'react'

/**
 * Navbars25
 */
export default function Navbars25({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars25" {...props}>
      {children}
    </div>
  )
}