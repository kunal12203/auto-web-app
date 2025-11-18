import { useState, useEffect } from 'react'

/**
 * Tours06
 */
export default function Tours06({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tours06" {...props}>
      {children}
    </div>
  )
}