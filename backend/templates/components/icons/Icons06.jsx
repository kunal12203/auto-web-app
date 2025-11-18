import { useState, useEffect } from 'react'

/**
 * Icons06
 */
export default function Icons06({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="icons06" {...props}>
      {children}
    </div>
  )
}