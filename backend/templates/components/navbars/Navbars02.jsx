import { useState, useEffect } from 'react'

/**
 * Navbars02
 */
export default function Navbars02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars02" {...props}>
      {children}
    </div>
  )
}