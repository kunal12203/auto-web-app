import { useState, useEffect } from 'react'

/**
 * Adminwidgets18
 */
export default function Adminwidgets18({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="adminwidgets18" {...props}>
      {children}
    </div>
  )
}