import { useState, useEffect } from 'react'

/**
 * Fileuploaders15
 */
export default function Fileuploaders15({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders15" {...props}>
      {children}
    </div>
  )
}