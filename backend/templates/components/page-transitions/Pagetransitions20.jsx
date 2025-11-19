import { useState, useEffect } from 'react'

/**
 * Pagetransitions20
 */
export default function Pagetransitions20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="pagetransitions20" {...props}>
      {children}
    </div>
  )
}