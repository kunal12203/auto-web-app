import { useState, useEffect } from 'react'

/**
 * Codeeditors01
 */
export default function Codeeditors01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="codeeditors01" {...props}>
      {children}
    </div>
  )
}