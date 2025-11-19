import { useState, useEffect } from 'react'

/**
 * Datetimepickers21
 */
export default function Datetimepickers21({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers21" {...props}>
      {children}
    </div>
  )
}