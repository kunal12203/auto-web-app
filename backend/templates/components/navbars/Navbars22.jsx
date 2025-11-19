import { useState, useEffect } from 'react'

/**
 * Navbars22
 */
export default function Navbars22({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars22" {...props}>
      {children}
    </div>
  )
}