import { useState, useEffect } from 'react'

/**
 * Tours05
 */
export default function Tours05({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tours05" {...props}>
      {children}
    </div>
  )
}