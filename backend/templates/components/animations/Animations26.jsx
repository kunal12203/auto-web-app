import { useState, useEffect } from 'react'

/**
 * Animations26
 */
export default function Animations26({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations26" {...props}>
      {children}
    </div>
  )
}