import { useState, useEffect } from 'react'

/**
 * Icons03
 */
export default function Icons03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="icons03" {...props}>
      {children}
    </div>
  )
}