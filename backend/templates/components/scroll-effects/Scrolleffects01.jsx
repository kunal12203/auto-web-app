import { useState, useEffect } from 'react'

/**
 * Scrolleffects01
 */
export default function Scrolleffects01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="scrolleffects01" {...props}>
      {children}
    </div>
  )
}