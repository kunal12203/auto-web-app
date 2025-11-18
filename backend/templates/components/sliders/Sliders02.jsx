import { useState, useEffect } from 'react'

/**
 * Sliders02
 */
export default function Sliders02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders02" {...props}>
      {children}
    </div>
  )
}