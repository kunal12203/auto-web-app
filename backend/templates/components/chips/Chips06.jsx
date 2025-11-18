import { useState, useEffect } from 'react'

/**
 * Chips06
 */
export default function Chips06({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="chips06" {...props}>
      {children}
    </div>
  )
}