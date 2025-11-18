import { useState, useEffect } from 'react'

/**
 * Scrolleffects02
 */
export default function Scrolleffects02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="scrolleffects02" {...props}>
      {children}
    </div>
  )
}