import { useState, useEffect } from 'react'

/**
 * Animations30
 */
export default function Animations30({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations30" {...props}>
      {children}
    </div>
  )
}