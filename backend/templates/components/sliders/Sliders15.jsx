import { useState, useEffect } from 'react'

/**
 * Sliders15
 */
export default function Sliders15({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders15" {...props}>
      {children}
    </div>
  )
}