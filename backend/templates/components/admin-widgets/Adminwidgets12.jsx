import { useState, useEffect } from 'react'

/**
 * Adminwidgets12
 */
export default function Adminwidgets12({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="adminwidgets12" {...props}>
      {children}
    </div>
  )
}