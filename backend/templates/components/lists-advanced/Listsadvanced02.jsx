import { useState, useEffect } from 'react'

/**
 * Listsadvanced02
 */
export default function Listsadvanced02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="listsadvanced02" {...props}>
      {children}
    </div>
  )
}