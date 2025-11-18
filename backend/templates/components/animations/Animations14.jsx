import { useState, useEffect } from 'react'

/**
 * Animations14
 */
export default function Animations14({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations14" {...props}>
      {children}
    </div>
  )
}