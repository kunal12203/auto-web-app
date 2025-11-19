import { useState, useEffect } from 'react'

/**
 * Dividers01
 */
export default function Dividers01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="dividers01" {...props}>
      {children}
    </div>
  )
}