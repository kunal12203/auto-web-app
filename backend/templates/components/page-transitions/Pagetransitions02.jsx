import { useState, useEffect } from 'react'

/**
 * Pagetransitions02
 */
export default function Pagetransitions02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="pagetransitions02" {...props}>
      {children}
    </div>
  )
}