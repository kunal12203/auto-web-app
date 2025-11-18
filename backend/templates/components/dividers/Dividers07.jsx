import { useState, useEffect } from 'react'

/**
 * Dividers07
 */
export default function Dividers07({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="dividers07" {...props}>
      {children}
    </div>
  )
}