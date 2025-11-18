import { useState, useEffect } from 'react'

/**
 * Datetimepickers06
 */
export default function Datetimepickers06({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers06" {...props}>
      {children}
    </div>
  )
}