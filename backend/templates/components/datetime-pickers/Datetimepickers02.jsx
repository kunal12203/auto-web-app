import { useState, useEffect } from 'react'

/**
 * Datetimepickers02
 */
export default function Datetimepickers02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="datetimepickers02" {...props}>
      {children}
    </div>
  )
}