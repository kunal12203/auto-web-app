import { useState, useEffect } from 'react'

/**
 * Adminwidgets08
 */
export default function Adminwidgets08({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="adminwidgets08" {...props}>
      {children}
    </div>
  )
}