import { useState, useEffect } from 'react'

/**
 * Texteditors01
 */
export default function Texteditors01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="texteditors01" {...props}>
      {children}
    </div>
  )
}