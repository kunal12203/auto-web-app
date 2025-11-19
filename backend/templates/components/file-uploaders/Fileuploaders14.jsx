import { useState, useEffect } from 'react'

/**
 * Fileuploaders14
 */
export default function Fileuploaders14({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders14" {...props}>
      {children}
    </div>
  )
}