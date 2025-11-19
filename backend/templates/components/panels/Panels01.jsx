import { useState, useEffect } from 'react'

/**
 * Panels01
 */
export default function Panels01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="panels01" {...props}>
      {children}
    </div>
  )
}