import { useState, useEffect } from 'react'

/**
 * Animations13
 */
export default function Animations13({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations13" {...props}>
      {children}
    </div>
  )
}