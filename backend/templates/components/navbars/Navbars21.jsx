import { useState, useEffect } from 'react'

/**
 * Navbars21
 */
export default function Navbars21({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars21" {...props}>
      {children}
    </div>
  )
}