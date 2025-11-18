import { useState, useEffect } from 'react'

/**
 * Animations25
 */
export default function Animations25({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations25" {...props}>
      {children}
    </div>
  )
}