import { useState, useEffect } from 'react'

/**
 * Datetimepickers26
 */
export default function Datetimepickers26({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers26" {...props}>
      {children}
    </div>
  )
}