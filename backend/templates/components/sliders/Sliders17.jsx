import { useState, useEffect } from 'react'

/**
 * Sliders17
 */
export default function Sliders17({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders17" {...props}>
      {children}
    </div>
  )
}