import { useState, useEffect } from 'react'

/**
 * Dividers04
 */
export default function Dividers04({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="dividers04" {...props}>
      {children}
    </div>
  )
}