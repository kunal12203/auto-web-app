import { useState, useEffect } from 'react'

/**
 * Dividers12
 */
export default function Dividers12({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="dividers12" {...props}>
      {children}
    </div>
  )
}