import { useState, useEffect } from 'react'

/**
 * Datetimepickers03
 */
export default function Datetimepickers03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers03" {...props}>
      {children}
    </div>
  )
}