import { useState, useEffect } from 'react'

/**
 * Scrolleffects14
 */
export default function Scrolleffects14({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="scrolleffects14" {...props}>
      {children}
    </div>
  )
}