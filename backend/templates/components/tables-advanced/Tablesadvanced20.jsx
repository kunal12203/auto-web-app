import { useState, useEffect } from 'react'

/**
 * Tablesadvanced20
 */
export default function Tablesadvanced20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tablesadvanced20" {...props}>
      {children}
    </div>
  )
}