import { useState, useEffect } from 'react'

/**
 * Animations24
 */
export default function Animations24({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations24" {...props}>
      {children}
    </div>
  )
}