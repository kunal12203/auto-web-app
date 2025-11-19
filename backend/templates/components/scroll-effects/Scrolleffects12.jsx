import { useState, useEffect } from 'react'

/**
 * Scrolleffects12
 */
export default function Scrolleffects12({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="scrolleffects12" {...props}>
      {children}
    </div>
  )
}