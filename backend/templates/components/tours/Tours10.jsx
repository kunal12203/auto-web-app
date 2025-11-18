import { useState, useEffect } from 'react'

/**
 * Tours10
 */
export default function Tours10({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tours10" {...props}>
      {children}
    </div>
  )
}