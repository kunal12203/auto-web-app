import { useState, useEffect } from 'react'

/**
 * Datetimepickers13
 */
export default function Datetimepickers13({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers13" {...props}>
      {children}
    </div>
  )
}