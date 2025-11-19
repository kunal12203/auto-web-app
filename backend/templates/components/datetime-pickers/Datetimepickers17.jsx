import { useState, useEffect } from 'react'

/**
 * Datetimepickers17
 */
export default function Datetimepickers17({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers17" {...props}>
      {children}
    </div>
  )
}