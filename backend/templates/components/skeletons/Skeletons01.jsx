import { useState, useEffect } from 'react'

/**
 * Skeletons01
 */
export default function Skeletons01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="skeletons01" {...props}>
      {children}
    </div>
  )
}