import { useState, useEffect } from 'react'

/**
 * Tours09
 */
export default function Tours09({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tours09" {...props}>
      {children}
    </div>
  )
}