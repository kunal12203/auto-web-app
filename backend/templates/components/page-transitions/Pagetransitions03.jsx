import { useState, useEffect } from 'react'

/**
 * Pagetransitions03
 */
export default function Pagetransitions03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="pagetransitions03" {...props}>
      {children}
    </div>
  )
}