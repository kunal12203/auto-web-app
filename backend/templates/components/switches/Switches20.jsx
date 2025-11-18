import { useState, useEffect } from 'react'

/**
 * Switches20
 */
export default function Switches20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="switches20" {...props}>
      {children}
    </div>
  )
}