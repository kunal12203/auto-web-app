import { useState, useEffect } from 'react'

/**
 * Icons04
 */
export default function Icons04({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="icons04" {...props}>
      {children}
    </div>
  )
}