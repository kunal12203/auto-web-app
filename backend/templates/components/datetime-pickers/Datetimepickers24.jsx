import { useState, useEffect } from 'react'

/**
 * Datetimepickers24
 */
export default function Datetimepickers24({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers24" {...props}>
      {children}
    </div>
  )
}