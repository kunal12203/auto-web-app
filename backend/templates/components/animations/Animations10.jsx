import { useState, useEffect } from 'react'

/**
 * Animations10
 */
export default function Animations10({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations10" {...props}>
      {children}
    </div>
  )
}