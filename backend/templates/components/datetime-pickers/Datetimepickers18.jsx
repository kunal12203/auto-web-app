import { useState, useEffect } from 'react'

/**
 * Datetimepickers18
 */
export default function Datetimepickers18({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers18" {...props}>
      {children}
    </div>
  )
}