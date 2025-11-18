import { useState, useEffect } from 'react'

/**
 * Scrolleffects05
 */
export default function Scrolleffects05({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="scrolleffects05" {...props}>
      {children}
    </div>
  )
}