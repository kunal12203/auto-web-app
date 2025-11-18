import { useState, useEffect } from 'react'

/**
 * Datetimepickers05
 */
export default function Datetimepickers05({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers05" {...props}>
      {children}
    </div>
  )
}