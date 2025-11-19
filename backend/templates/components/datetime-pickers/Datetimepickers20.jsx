import { useState, useEffect } from 'react'

/**
 * Datetimepickers20
 */
export default function Datetimepickers20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers20" {...props}>
      {children}
    </div>
  )
}