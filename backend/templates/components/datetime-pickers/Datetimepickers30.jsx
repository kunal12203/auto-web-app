import { useState, useEffect } from 'react'

/**
 * Datetimepickers30
 */
export default function Datetimepickers30({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers30" {...props}>
      {children}
    </div>
  )
}