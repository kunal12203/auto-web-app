import { useState, useEffect } from 'react'

/**
 * Dividers15
 */
export default function Dividers15({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="dividers15" {...props}>
      {children}
    </div>
  )
}