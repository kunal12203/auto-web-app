import { useState, useEffect } from 'react'

/**
 * Sliders20
 */
export default function Sliders20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders20" {...props}>
      {children}
    </div>
  )
}