import { useState, useEffect } from 'react'

/**
 * Panels05
 */
export default function Panels05({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="panels05" {...props}>
      {children}
    </div>
  )
}