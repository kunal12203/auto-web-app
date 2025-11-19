import { useState, useEffect } from 'react'

/**
 * Navbars12
 */
export default function Navbars12({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars12" {...props}>
      {children}
    </div>
  )
}