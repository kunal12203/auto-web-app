import { useState, useEffect } from 'react'

/**
 * Appbars14
 */
export default function Appbars14({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="appbars14" {...props}>
      {children}
    </div>
  )
}