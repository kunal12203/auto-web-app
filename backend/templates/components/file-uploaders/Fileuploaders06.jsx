import { useState, useEffect } from 'react'

/**
 * Fileuploaders06
 */
export default function Fileuploaders06({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders06" {...props}>
      {children}
    </div>
  )
}