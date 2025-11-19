import { useState, useEffect } from 'react'

/**
 * Panels17
 */
export default function Panels17({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="panels17" {...props}>
      {children}
    </div>
  )
}