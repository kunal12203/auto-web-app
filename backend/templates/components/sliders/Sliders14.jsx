import { useState, useEffect } from 'react'

/**
 * Sliders14
 */
export default function Sliders14({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders14" {...props}>
      {children}
    </div>
  )
}