import { useState, useEffect } from 'react'

/**
 * Parallax05
 */
export default function Parallax05({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="parallax05" {...props}>
      {children}
    </div>
  )
}