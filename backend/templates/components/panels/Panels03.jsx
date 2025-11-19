import { useState, useEffect } from 'react'

/**
 * Panels03
 */
export default function Panels03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="panels03" {...props}>
      {children}
    </div>
  )
}