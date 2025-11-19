import { useState, useEffect } from 'react'

/**
 * Animations20
 */
export default function Animations20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations20" {...props}>
      {children}
    </div>
  )
}