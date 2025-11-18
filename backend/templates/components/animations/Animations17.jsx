import { useState, useEffect } from 'react'

/**
 * Animations17
 */
export default function Animations17({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations17" {...props}>
      {children}
    </div>
  )
}