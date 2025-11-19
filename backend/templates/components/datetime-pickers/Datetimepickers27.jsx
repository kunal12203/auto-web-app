import { useState, useEffect } from 'react'

/**
 * Datetimepickers27
 */
export default function Datetimepickers27({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers27" {...props}>
      {children}
    </div>
  )
}