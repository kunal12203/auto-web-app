import { useState, useEffect } from 'react'

/**
 * Fileuploaders02
 */
export default function Fileuploaders02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders02" {...props}>
      {children}
    </div>
  )
}