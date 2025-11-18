import { useState, useEffect } from 'react'

/**
 * Multiselect12
 */
export default function Multiselect12({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="multiselect12" {...props}>
      {children}
    </div>
  )
}