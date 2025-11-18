import { useState, useEffect } from 'react'

/**
 * Navbars10
 */
export default function Navbars10({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars10" {...props}>
      {children}
    </div>
  )
}