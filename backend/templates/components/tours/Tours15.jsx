import { useState, useEffect } from 'react'

/**
 * Tours15
 */
export default function Tours15({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tours15" {...props}>
      {children}
    </div>
  )
}