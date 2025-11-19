import { useState, useEffect } from 'react'

/**
 * Adminwidgets20
 */
export default function Adminwidgets20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="adminwidgets20" {...props}>
      {children}
    </div>
  )
}