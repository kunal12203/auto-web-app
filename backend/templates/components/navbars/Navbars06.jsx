import { useState, useEffect } from 'react'

/**
 * Navbars06
 */
export default function Navbars06({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars06" {...props}>
      {children}
    </div>
  )
}