import { useState, useEffect } from 'react'

/**
 * Navbars17
 */
export default function Navbars17({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars17" {...props}>
      {children}
    </div>
  )
}