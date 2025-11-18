import { useState, useEffect } from 'react'

/**
 * Scrolleffects18
 */
export default function Scrolleffects18({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="scrolleffects18" {...props}>
      {children}
    </div>
  )
}