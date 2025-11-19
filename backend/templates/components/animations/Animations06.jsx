import { useState, useEffect } from 'react'

/**
 * Animations06
 */
export default function Animations06({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations06" {...props}>
      {children}
    </div>
  )
}