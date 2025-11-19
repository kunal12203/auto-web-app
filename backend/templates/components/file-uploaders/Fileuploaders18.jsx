import { useState, useEffect } from 'react'

/**
 * Fileuploaders18
 */
export default function Fileuploaders18({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders18" {...props}>
      {children}
    </div>
  )
}