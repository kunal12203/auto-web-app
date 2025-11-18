import { useState, useEffect } from 'react'

/**
 * Fileuploaders12
 */
export default function Fileuploaders12({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders12" {...props}>
      {children}
    </div>
  )
}