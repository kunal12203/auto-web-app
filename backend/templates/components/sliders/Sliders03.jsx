import { useState, useEffect } from 'react'

/**
 * Sliders03
 */
export default function Sliders03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="sliders03" {...props}>
      {children}
    </div>
  )
}