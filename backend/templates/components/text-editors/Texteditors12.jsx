import { useState, useEffect } from 'react'

/**
 * Texteditors12
 */
export default function Texteditors12({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="texteditors12" {...props}>
      {children}
    </div>
  )
}