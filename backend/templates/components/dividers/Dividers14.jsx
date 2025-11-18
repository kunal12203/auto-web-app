import { useState, useEffect } from 'react'

/**
 * Dividers14
 */
export default function Dividers14({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="dividers14" {...props}>
      {children}
    </div>
  )
}