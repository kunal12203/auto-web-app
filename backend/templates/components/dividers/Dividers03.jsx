import { useState, useEffect } from 'react'

/**
 * Dividers03
 */
export default function Dividers03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="dividers03" {...props}>
      {children}
    </div>
  )
}