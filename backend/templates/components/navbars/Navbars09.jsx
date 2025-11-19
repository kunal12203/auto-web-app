import { useState, useEffect } from 'react'

/**
 * Navbars09
 */
export default function Navbars09({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars09" {...props}>
      {children}
    </div>
  )
}