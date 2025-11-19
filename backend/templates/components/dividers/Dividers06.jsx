import { useState, useEffect } from 'react'

/**
 * Dividers06
 */
export default function Dividers06({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="dividers06" {...props}>
      {children}
    </div>
  )
}