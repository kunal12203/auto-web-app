import { useState, useEffect } from 'react'

/**
 * Appbars13
 */
export default function Appbars13({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="appbars13" {...props}>
      {children}
    </div>
  )
}