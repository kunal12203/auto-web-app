import { useState, useEffect } from 'react'

/**
 * Animations27
 */
export default function Animations27({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations27" {...props}>
      {children}
    </div>
  )
}