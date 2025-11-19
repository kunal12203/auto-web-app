import { useState, useEffect } from 'react'

/**
 * Tours01
 */
export default function Tours01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tours01" {...props}>
      {children}
    </div>
  )
}