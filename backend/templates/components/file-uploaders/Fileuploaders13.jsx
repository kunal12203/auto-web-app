import { useState, useEffect } from 'react'

/**
 * Fileuploaders13
 */
export default function Fileuploaders13({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders13" {...props}>
      {children}
    </div>
  )
}