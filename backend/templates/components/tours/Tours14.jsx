import { useState, useEffect } from 'react'

/**
 * Tours14
 */
export default function Tours14({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tours14" {...props}>
      {children}
    </div>
  )
}