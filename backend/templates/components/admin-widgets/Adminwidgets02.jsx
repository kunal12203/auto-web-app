import { useState, useEffect } from 'react'

/**
 * Adminwidgets02
 */
export default function Adminwidgets02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="adminwidgets02" {...props}>
      {children}
    </div>
  )
}