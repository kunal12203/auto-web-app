import { useState, useEffect } from 'react'

/**
 * Fileuploaders10
 */
export default function Fileuploaders10({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders10" {...props}>
      {children}
    </div>
  )
}