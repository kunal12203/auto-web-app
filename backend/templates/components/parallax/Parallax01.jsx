import { useState, useEffect } from 'react'

/**
 * Parallax01
 */
export default function Parallax01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="parallax01" {...props}>
      {children}
    </div>
  )
}