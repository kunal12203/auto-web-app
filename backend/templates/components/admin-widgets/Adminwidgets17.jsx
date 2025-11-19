import { useState, useEffect } from 'react'

/**
 * Adminwidgets17
 */
export default function Adminwidgets17({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="adminwidgets17" {...props}>
      {children}
    </div>
  )
}