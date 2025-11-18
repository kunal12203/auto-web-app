import { useState, useEffect } from 'react'

/**
 * Parallax04
 */
export default function Parallax04({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="parallax04" {...props}>
      {children}
    </div>
  )
}