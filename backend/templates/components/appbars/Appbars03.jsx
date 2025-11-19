import { useState, useEffect } from 'react'

/**
 * Appbars03
 */
export default function Appbars03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="appbars03" {...props}>
      {children}
    </div>
  )
}