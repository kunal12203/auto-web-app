import { useState, useEffect } from 'react'

/**
 * Fileuploaders24
 */
export default function Fileuploaders24({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders24" {...props}>
      {children}
    </div>
  )
}