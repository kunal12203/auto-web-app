import { useState, useEffect } from 'react'

/**
 * Adminwidgets13
 */
export default function Adminwidgets13({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="adminwidgets13" {...props}>
      {children}
    </div>
  )
}