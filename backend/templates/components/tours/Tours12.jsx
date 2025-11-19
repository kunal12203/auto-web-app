import { useState, useEffect } from 'react'

/**
 * Tours12
 */
export default function Tours12({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tours12" {...props}>
      {children}
    </div>
  )
}