import { useState, useEffect } from 'react'

/**
 * Icons17
 */
export default function Icons17({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="icons17" {...props}>
      {children}
    </div>
  )
}