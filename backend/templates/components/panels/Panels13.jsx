import { useState, useEffect } from 'react'

/**
 * Panels13
 */
export default function Panels13({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="panels13" {...props}>
      {children}
    </div>
  )
}