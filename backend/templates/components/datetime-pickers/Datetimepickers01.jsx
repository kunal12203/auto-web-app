import { useState, useEffect } from 'react'

/**
 * Datetimepickers01
 */
export default function Datetimepickers01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers01" {...props}>
      {children}
    </div>
  )
}