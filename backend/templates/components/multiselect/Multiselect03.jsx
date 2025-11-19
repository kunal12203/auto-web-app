import { useState, useEffect } from 'react'

/**
 * Multiselect03
 */
export default function Multiselect03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="multiselect03" {...props}>
      {children}
    </div>
  )
}