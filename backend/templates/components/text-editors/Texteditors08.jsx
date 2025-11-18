import { useState, useEffect } from 'react'

/**
 * Texteditors08
 */
export default function Texteditors08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="texteditors08" {...props}>
      {children}
    </div>
  )
}