import { useState, useEffect } from 'react'

/**
 * Chips02
 */
export default function Chips02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="chips02" {...props}>
      {children}
    </div>
  )
}