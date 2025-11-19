import { useState, useEffect } from 'react'

/**
 * Animations04
 */
export default function Animations04({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations04" {...props}>
      {children}
    </div>
  )
}