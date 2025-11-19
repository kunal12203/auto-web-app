import { useState, useEffect } from 'react'

/**
 * Animations08
 */
export default function Animations08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations08" {...props}>
      {children}
    </div>
  )
}