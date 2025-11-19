import { useState, useEffect } from 'react'

/**
 * Adminwidgets03
 */
export default function Adminwidgets03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="adminwidgets03" {...props}>
      {children}
    </div>
  )
}