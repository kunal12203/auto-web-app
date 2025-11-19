import { useState, useEffect } from 'react'

/**
 * Fileuploaders21
 */
export default function Fileuploaders21({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders21" {...props}>
      {children}
    </div>
  )
}