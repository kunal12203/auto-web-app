import { useState, useEffect } from 'react'

/**
 * Texteditors02
 */
export default function Texteditors02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="texteditors02" {...props}>
      {children}
    </div>
  )
}