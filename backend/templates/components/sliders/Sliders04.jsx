import { useState, useEffect } from 'react'

/**
 * Sliders04
 */
export default function Sliders04({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders04" {...props}>
      {children}
    </div>
  )
}