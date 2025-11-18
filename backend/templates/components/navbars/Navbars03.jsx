import { useState, useEffect } from 'react'

/**
 * Navbars03
 */
export default function Navbars03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars03" {...props}>
      {children}
    </div>
  )
}