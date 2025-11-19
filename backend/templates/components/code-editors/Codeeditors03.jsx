import { useState, useEffect } from 'react'

/**
 * Codeeditors03
 */
export default function Codeeditors03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="codeeditors03" {...props}>
      {children}
    </div>
  )
}