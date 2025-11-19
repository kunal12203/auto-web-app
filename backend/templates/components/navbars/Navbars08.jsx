import { useState, useEffect } from 'react'

/**
 * Navbars08
 */
export default function Navbars08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars08" {...props}>
      {children}
    </div>
  )
}