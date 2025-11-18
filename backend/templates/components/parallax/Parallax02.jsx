import { useState, useEffect } from 'react'

/**
 * Parallax02
 */
export default function Parallax02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="parallax02" {...props}>
      {children}
    </div>
  )
}