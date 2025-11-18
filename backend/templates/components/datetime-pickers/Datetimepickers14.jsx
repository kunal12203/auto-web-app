import { useState, useEffect } from 'react'

/**
 * Datetimepickers14
 */
export default function Datetimepickers14({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers14" {...props}>
      {children}
    </div>
  )
}