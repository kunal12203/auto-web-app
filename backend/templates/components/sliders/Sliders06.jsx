import { useState, useEffect } from 'react'

/**
 * Sliders06
 */
export default function Sliders06({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders06" {...props}>
      {children}
    </div>
  )
}