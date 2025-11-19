import { useState, useEffect } from 'react'

/**
 * Animations23
 */
export default function Animations23({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations23" {...props}>
      {children}
    </div>
  )
}