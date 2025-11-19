import { useState, useEffect } from 'react'

/**
 * Tours03
 */
export default function Tours03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tours03" {...props}>
      {children}
    </div>
  )
}