import { useState, useEffect } from 'react'

/**
 * Pagetransitions18
 */
export default function Pagetransitions18({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="pagetransitions18" {...props}>
      {children}
    </div>
  )
}