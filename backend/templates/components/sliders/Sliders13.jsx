import { useState, useEffect } from 'react'

/**
 * Sliders13
 */
export default function Sliders13({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders13" {...props}>
      {children}
    </div>
  )
}