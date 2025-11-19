import { useState, useEffect } from 'react'

/**
 * Adminwidgets14
 */
export default function Adminwidgets14({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="adminwidgets14" {...props}>
      {children}
    </div>
  )
}