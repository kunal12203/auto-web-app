import { useState, useEffect } from 'react'

/**
 * Tours04
 */
export default function Tours04({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tours04" {...props}>
      {children}
    </div>
  )
}