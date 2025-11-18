import { useState, useEffect } from 'react'

/**
 * Panels06
 */
export default function Panels06({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="panels06" {...props}>
      {children}
    </div>
  )
}