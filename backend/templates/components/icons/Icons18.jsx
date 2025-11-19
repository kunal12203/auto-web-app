import { useState, useEffect } from 'react'

/**
 * Icons18
 */
export default function Icons18({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="icons18" {...props}>
      {children}
    </div>
  )
}