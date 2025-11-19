import { useState, useEffect } from 'react'

/**
 * Fileuploaders03
 */
export default function Fileuploaders03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders03" {...props}>
      {children}
    </div>
  )
}