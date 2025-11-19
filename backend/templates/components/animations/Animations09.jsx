import { useState, useEffect } from 'react'

/**
 * Animations09
 */
export default function Animations09({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations09" {...props}>
      {children}
    </div>
  )
}