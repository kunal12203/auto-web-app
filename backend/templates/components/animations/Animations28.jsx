import { useState, useEffect } from 'react'

/**
 * Animations28
 */
export default function Animations28({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations28" {...props}>
      {children}
    </div>
  )
}