import { useState, useEffect } from 'react'

/**
 * Dividers13
 */
export default function Dividers13({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="dividers13" {...props}>
      {children}
    </div>
  )
}