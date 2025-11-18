import { useState, useEffect } from 'react'

/**
 * Tours02
 */
export default function Tours02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tours02" {...props}>
      {children}
    </div>
  )
}