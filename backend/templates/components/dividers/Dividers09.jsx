import { useState, useEffect } from 'react'

/**
 * Dividers09
 */
export default function Dividers09({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="dividers09" {...props}>
      {children}
    </div>
  )
}