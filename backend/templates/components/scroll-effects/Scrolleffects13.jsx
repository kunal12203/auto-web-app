import { useState, useEffect } from 'react'

/**
 * Scrolleffects13
 */
export default function Scrolleffects13({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="scrolleffects13" {...props}>
      {children}
    </div>
  )
}