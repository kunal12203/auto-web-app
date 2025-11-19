import { useState, useEffect } from 'react'

/**
 * Scrolleffects08
 */
export default function Scrolleffects08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="scrolleffects08" {...props}>
      {children}
    </div>
  )
}