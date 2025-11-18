import { useState, useEffect } from 'react'

/**
 * Navbars24
 */
export default function Navbars24({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars24" {...props}>
      {children}
    </div>
  )
}