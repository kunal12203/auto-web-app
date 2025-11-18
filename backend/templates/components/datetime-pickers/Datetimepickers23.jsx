import { useState, useEffect } from 'react'

/**
 * Datetimepickers23
 */
export default function Datetimepickers23({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers23" {...props}>
      {children}
    </div>
  )
}