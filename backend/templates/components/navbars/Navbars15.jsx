import { useState, useEffect } from 'react'

/**
 * Navbars15
 */
export default function Navbars15({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars15" {...props}>
      {children}
    </div>
  )
}