import { useState, useEffect } from 'react'

/**
 * Parallax06
 */
export default function Parallax06({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="parallax06" {...props}>
      {children}
    </div>
  )
}