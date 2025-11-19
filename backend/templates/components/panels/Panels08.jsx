import { useState, useEffect } from 'react'

/**
 * Panels08
 */
export default function Panels08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="panels08" {...props}>
      {children}
    </div>
  )
}