import { useState, useEffect } from 'react'

/**
 * Panels04
 */
export default function Panels04({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="panels04" {...props}>
      {children}
    </div>
  )
}