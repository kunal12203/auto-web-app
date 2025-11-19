import { useState, useEffect } from 'react'

/**
 * Fileuploaders25
 */
export default function Fileuploaders25({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders25" {...props}>
      {children}
    </div>
  )
}