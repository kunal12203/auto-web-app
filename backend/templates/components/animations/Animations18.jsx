import { useState, useEffect } from 'react'

/**
 * Animations18
 */
export default function Animations18({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations18" {...props}>
      {children}
    </div>
  )
}