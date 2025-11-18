import { useState, useEffect } from 'react'

/**
 * Sidebarsadvanced20
 */
export default function Sidebarsadvanced20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sidebarsadvanced20" {...props}>
      {children}
    </div>
  )
}