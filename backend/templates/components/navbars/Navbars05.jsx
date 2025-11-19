import { useState, useEffect } from 'react'

/**
 * Navbars05
 */
export default function Navbars05({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars05" {...props}>
      {children}
    </div>
  )
}