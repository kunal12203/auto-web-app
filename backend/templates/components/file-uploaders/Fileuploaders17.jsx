import { useState, useEffect } from 'react'

/**
 * Fileuploaders17
 */
export default function Fileuploaders17({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders17" {...props}>
      {children}
    </div>
  )
}