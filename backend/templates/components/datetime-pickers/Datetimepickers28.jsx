import { useState, useEffect } from 'react'

/**
 * Datetimepickers28
 */
export default function Datetimepickers28({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers28" {...props}>
      {children}
    </div>
  )
}