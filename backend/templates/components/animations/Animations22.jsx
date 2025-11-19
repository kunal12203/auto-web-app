import { useState, useEffect } from 'react'

/**
 * Animations22
 */
export default function Animations22({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations22" {...props}>
      {children}
    </div>
  )
}