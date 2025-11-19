import { useState, useEffect } from 'react'

/**
 * Multiselect01
 */
export default function Multiselect01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="multiselect01" {...props}>
      {children}
    </div>
  )
}