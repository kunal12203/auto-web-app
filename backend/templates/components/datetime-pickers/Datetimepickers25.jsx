import { useState, useEffect } from 'react'

/**
 * Datetimepickers25
 */
export default function Datetimepickers25({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers25" {...props}>
      {children}
    </div>
  )
}