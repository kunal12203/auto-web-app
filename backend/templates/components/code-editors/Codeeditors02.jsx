import { useState, useEffect } from 'react'

/**
 * Codeeditors02
 */
export default function Codeeditors02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="codeeditors02" {...props}>
      {children}
    </div>
  )
}