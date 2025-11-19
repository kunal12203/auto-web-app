import { useState, useEffect } from 'react'

/**
 * Texteditors03
 */
export default function Texteditors03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="texteditors03" {...props}>
      {children}
    </div>
  )
}