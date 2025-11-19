import { useState, useEffect } from 'react'

/**
 * Sliders10
 */
export default function Sliders10({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders10" {...props}>
      {children}
    </div>
  )
}