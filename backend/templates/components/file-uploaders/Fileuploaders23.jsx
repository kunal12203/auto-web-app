import { useState, useEffect } from 'react'

/**
 * Fileuploaders23
 */
export default function Fileuploaders23({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders23" {...props}>
      {children}
    </div>
  )
}