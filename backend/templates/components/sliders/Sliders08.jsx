import { useState, useEffect } from 'react'

/**
 * Sliders08
 */
export default function Sliders08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders08" {...props}>
      {children}
    </div>
  )
}