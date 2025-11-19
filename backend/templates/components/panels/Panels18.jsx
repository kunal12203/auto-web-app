import { useState, useEffect } from 'react'

/**
 * Panels18
 */
export default function Panels18({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="panels18" {...props}>
      {children}
    </div>
  )
}