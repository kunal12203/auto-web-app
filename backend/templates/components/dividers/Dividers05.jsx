import { useState, useEffect } from 'react'

/**
 * Dividers05
 */
export default function Dividers05({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="dividers05" {...props}>
      {children}
    </div>
  )
}