import { useState, useEffect } from 'react'

/**
 * Skeletons20
 */
export default function Skeletons20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="skeletons20" {...props}>
      {children}
    </div>
  )
}