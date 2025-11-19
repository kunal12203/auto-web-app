import { useState, useEffect } from 'react'

/**
 * Adminwidgets06
 */
export default function Adminwidgets06({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="adminwidgets06" {...props}>
      {children}
    </div>
  )
}