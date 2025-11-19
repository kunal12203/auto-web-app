import { useState, useEffect } from 'react'

/**
 * Datetimepickers15
 */
export default function Datetimepickers15({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers15" {...props}>
      {children}
    </div>
  )
}