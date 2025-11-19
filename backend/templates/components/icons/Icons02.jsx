import { useState, useEffect } from 'react'

/**
 * Icons02
 */
export default function Icons02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="icons02" {...props}>
      {children}
    </div>
  )
}