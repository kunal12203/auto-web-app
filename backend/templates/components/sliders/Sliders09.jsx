import { useState, useEffect } from 'react'

/**
 * Sliders09
 */
export default function Sliders09({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders09" {...props}>
      {children}
    </div>
  )
}