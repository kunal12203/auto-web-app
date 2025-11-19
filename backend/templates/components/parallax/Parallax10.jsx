import { useState, useEffect } from 'react'

/**
 * Parallax10
 */
export default function Parallax10({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="parallax10" {...props}>
      {children}
    </div>
  )
}