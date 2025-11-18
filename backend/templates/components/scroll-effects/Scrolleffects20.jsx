import { useState, useEffect } from 'react'

/**
 * Scrolleffects20
 */
export default function Scrolleffects20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="scrolleffects20" {...props}>
      {children}
    </div>
  )
}