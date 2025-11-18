import { useState, useEffect } from 'react'

/**
 * Multiselect08
 */
export default function Multiselect08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="multiselect08" {...props}>
      {children}
    </div>
  )
}