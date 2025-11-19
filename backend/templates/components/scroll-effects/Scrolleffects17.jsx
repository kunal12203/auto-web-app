import { useState, useEffect } from 'react'

/**
 * Scrolleffects17
 */
export default function Scrolleffects17({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="scrolleffects17" {...props}>
      {children}
    </div>
  )
}