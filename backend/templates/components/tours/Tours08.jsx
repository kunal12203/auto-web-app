import { useState, useEffect } from 'react'

/**
 * Tours08
 */
export default function Tours08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tours08" {...props}>
      {children}
    </div>
  )
}