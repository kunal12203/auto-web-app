import { useState, useEffect } from 'react'

/**
 * Panels12
 */
export default function Panels12({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="panels12" {...props}>
      {children}
    </div>
  )
}