import { useState, useEffect } from 'react'

/**
 * Appbars06
 */
export default function Appbars06({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="appbars06" {...props}>
      {children}
    </div>
  )
}