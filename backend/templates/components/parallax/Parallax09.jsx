import { useState, useEffect } from 'react'

/**
 * Parallax09
 */
export default function Parallax09({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="parallax09" {...props}>
      {children}
    </div>
  )
}