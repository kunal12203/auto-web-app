import { useState, useEffect } from 'react'

/**
 * Icons12
 */
export default function Icons12({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="icons12" {...props}>
      {children}
    </div>
  )
}