import { useState, useEffect } from 'react'

/**
 * Multiselect02
 */
export default function Multiselect02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="multiselect02" {...props}>
      {children}
    </div>
  )
}