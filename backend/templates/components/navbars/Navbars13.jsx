import { useState, useEffect } from 'react'

/**
 * Navbars13
 */
export default function Navbars13({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars13" {...props}>
      {children}
    </div>
  )
}