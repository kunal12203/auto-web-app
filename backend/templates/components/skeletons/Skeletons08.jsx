import { useState, useEffect } from 'react'

/**
 * Skeletons08
 */
export default function Skeletons08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="skeletons08" {...props}>
      {children}
    </div>
  )
}