import { useState, useEffect } from 'react'

/**
 * Icons08
 */
export default function Icons08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="icons08" {...props}>
      {children}
    </div>
  )
}