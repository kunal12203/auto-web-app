import { useState, useEffect } from 'react'

/**
 * Datetimepickers08
 */
export default function Datetimepickers08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers08" {...props}>
      {children}
    </div>
  )
}