import { useState, useEffect } from 'react'

/**
 * Parallax07
 */
export default function Parallax07({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="parallax07" {...props}>
      {children}
    </div>
  )
}