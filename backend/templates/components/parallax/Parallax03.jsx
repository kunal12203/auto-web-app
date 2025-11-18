import { useState, useEffect } from 'react'

/**
 * Parallax03
 */
export default function Parallax03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="parallax03" {...props}>
      {children}
    </div>
  )
}