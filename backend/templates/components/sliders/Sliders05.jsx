import { useState, useEffect } from 'react'

/**
 * Sliders05
 */
export default function Sliders05({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders05" {...props}>
      {children}
    </div>
  )
}