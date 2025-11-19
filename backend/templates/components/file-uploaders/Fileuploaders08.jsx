import { useState, useEffect } from 'react'

/**
 * Fileuploaders08
 */
export default function Fileuploaders08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders08" {...props}>
      {children}
    </div>
  )
}