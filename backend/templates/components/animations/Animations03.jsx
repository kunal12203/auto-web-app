import { useState, useEffect } from 'react'

/**
 * Animations03
 */
export default function Animations03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations03" {...props}>
      {children}
    </div>
  )
}