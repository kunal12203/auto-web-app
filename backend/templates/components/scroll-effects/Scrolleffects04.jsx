import { useState, useEffect } from 'react'

/**
 * Scrolleffects04
 */
export default function Scrolleffects04({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="scrolleffects04" {...props}>
      {children}
    </div>
  )
}