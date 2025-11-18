import { useState, useEffect } from 'react'

/**
 * Animations12
 */
export default function Animations12({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations12" {...props}>
      {children}
    </div>
  )
}