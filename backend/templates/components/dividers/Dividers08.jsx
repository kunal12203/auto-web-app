import { useState, useEffect } from 'react'

/**
 * Dividers08
 */
export default function Dividers08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="dividers08" {...props}>
      {children}
    </div>
  )
}