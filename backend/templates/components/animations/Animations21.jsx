import { useState, useEffect } from 'react'

/**
 * Animations21
 */
export default function Animations21({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations21" {...props}>
      {children}
    </div>
  )
}