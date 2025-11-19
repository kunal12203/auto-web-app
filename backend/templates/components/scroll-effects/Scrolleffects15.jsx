import { useState, useEffect } from 'react'

/**
 * Scrolleffects15
 */
export default function Scrolleffects15({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="scrolleffects15" {...props}>
      {children}
    </div>
  )
}