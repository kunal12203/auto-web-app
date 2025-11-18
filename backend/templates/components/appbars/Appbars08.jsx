import { useState, useEffect } from 'react'

/**
 * Appbars08
 */
export default function Appbars08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="appbars08" {...props}>
      {children}
    </div>
  )
}