import { useState, useEffect } from 'react'

/**
 * Animations05
 */
export default function Animations05({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations05" {...props}>
      {children}
    </div>
  )
}