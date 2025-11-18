import { useState, useEffect } from 'react'

/**
 * Icons01
 */
export default function Icons01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="icons01" {...props}>
      {children}
    </div>
  )
}