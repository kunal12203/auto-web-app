import { useState, useEffect } from 'react'

/**
 * Parallax08
 */
export default function Parallax08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="parallax08" {...props}>
      {children}
    </div>
  )
}