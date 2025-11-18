import { useState, useEffect } from 'react'

/**
 * Panels14
 */
export default function Panels14({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="panels14" {...props}>
      {children}
    </div>
  )
}