import { useState, useEffect } from 'react'

/**
 * Navbars11
 */
export default function Navbars11({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars11" {...props}>
      {children}
    </div>
  )
}