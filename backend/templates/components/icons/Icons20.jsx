import { useState, useEffect } from 'react'

/**
 * Icons20
 */
export default function Icons20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="icons20" {...props}>
      {children}
    </div>
  )
}