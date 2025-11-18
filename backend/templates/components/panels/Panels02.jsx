import { useState, useEffect } from 'react'

/**
 * Panels02
 */
export default function Panels02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="panels02" {...props}>
      {children}
    </div>
  )
}