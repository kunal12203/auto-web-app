import { useState, useEffect } from 'react'

/**
 * Tours13
 */
export default function Tours13({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tours13" {...props}>
      {children}
    </div>
  )
}