import { useState, useEffect } from 'react'

/**
 * Adminwidgets10
 */
export default function Adminwidgets10({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="adminwidgets10" {...props}>
      {children}
    </div>
  )
}