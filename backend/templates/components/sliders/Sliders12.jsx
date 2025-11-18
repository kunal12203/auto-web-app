import { useState, useEffect } from 'react'

/**
 * Sliders12
 */
export default function Sliders12({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders12" {...props}>
      {children}
    </div>
  )
}