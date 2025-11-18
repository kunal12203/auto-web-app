import { useState, useEffect } from 'react'

/**
 * Datetimepickers12
 */
export default function Datetimepickers12({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers12" {...props}>
      {children}
    </div>
  )
}