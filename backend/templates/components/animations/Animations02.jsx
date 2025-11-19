import { useState, useEffect } from 'react'

/**
 * Animations02
 */
export default function Animations02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations02" {...props}>
      {children}
    </div>
  )
}