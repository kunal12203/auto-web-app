import { useState, useEffect } from 'react'

/**
 * Navbars18
 */
export default function Navbars18({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars18" {...props}>
      {children}
    </div>
  )
}