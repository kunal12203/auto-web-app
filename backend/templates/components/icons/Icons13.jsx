import { useState, useEffect } from 'react'

/**
 * Icons13
 */
export default function Icons13({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="icons13" {...props}>
      {children}
    </div>
  )
}