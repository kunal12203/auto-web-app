import { useState, useEffect } from 'react'

/**
 * Dividers10
 */
export default function Dividers10({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="dividers10" {...props}>
      {children}
    </div>
  )
}