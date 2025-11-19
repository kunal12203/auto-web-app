import { useState, useEffect } from 'react'

/**
 * Pagetransitions01
 */
export default function Pagetransitions01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="pagetransitions01" {...props}>
      {children}
    </div>
  )
}