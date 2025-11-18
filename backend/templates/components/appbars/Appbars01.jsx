import { useState, useEffect } from 'react'

/**
 * Appbars01
 */
export default function Appbars01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="appbars01" {...props}>
      {children}
    </div>
  )
}