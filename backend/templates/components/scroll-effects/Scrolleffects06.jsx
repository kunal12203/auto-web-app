import { useState, useEffect } from 'react'

/**
 * Scrolleffects06
 */
export default function Scrolleffects06({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="scrolleffects06" {...props}>
      {children}
    </div>
  )
}