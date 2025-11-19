import { useState, useEffect } from 'react'

/**
 * Skeletons18
 */
export default function Skeletons18({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="skeletons18" {...props}>
      {children}
    </div>
  )
}