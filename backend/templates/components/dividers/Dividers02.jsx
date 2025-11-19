import { useState, useEffect } from 'react'

/**
 * Dividers02
 */
export default function Dividers02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="dividers02" {...props}>
      {children}
    </div>
  )
}