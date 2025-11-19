import { useState, useEffect } from 'react'

/**
 * Sliders01
 */
export default function Sliders01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders01" {...props}>
      {children}
    </div>
  )
}