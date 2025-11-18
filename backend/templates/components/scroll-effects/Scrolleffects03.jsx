import { useState, useEffect } from 'react'

/**
 * Scrolleffects03
 */
export default function Scrolleffects03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="scrolleffects03" {...props}>
      {children}
    </div>
  )
}