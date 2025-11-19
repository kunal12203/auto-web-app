import { useState, useEffect } from 'react'

/**
 * Icons14
 */
export default function Icons14({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="icons14" {...props}>
      {children}
    </div>
  )
}