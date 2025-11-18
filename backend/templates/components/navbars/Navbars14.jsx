import { useState, useEffect } from 'react'

/**
 * Navbars14
 */
export default function Navbars14({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars14" {...props}>
      {children}
    </div>
  )
}