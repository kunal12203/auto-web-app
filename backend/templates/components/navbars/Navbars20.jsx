import { useState, useEffect } from 'react'

/**
 * Navbars20
 */
export default function Navbars20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars20" {...props}>
      {children}
    </div>
  )
}