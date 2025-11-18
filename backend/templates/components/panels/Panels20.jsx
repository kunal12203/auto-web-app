import { useState, useEffect } from 'react'

/**
 * Panels20
 */
export default function Panels20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="panels20" {...props}>
      {children}
    </div>
  )
}