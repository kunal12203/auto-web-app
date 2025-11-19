import { useState, useEffect } from 'react'

/**
 * Adminwidgets01
 */
export default function Adminwidgets01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="adminwidgets01" {...props}>
      {children}
    </div>
  )
}