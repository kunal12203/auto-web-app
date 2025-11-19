import { useState, useEffect } from 'react'

/**
 * Chips03
 */
export default function Chips03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="chips03" {...props}>
      {children}
    </div>
  )
}