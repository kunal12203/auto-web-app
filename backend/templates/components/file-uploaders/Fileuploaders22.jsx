import { useState, useEffect } from 'react'

/**
 * Fileuploaders22
 */
export default function Fileuploaders22({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders22" {...props}>
      {children}
    </div>
  )
}