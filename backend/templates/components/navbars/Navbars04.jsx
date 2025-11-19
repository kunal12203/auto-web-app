import { useState, useEffect } from 'react'

/**
 * Navbars04
 */
export default function Navbars04({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="navbars04" {...props}>
      {children}
    </div>
  )
}