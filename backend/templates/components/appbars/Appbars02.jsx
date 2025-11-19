import { useState, useEffect } from 'react'

/**
 * Appbars02
 */
export default function Appbars02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="appbars02" {...props}>
      {children}
    </div>
  )
}