import { useState, useEffect } from 'react'

/**
 * Navbars01
 */
export default function Navbars01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars01" {...props}>
      {children}
    </div>
  )
}