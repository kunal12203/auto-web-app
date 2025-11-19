import { useState, useEffect } from 'react'

/**
 * Sliders18
 */
export default function Sliders18({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders18" {...props}>
      {children}
    </div>
  )
}