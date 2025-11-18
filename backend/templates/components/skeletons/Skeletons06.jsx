import { useState, useEffect } from 'react'

/**
 * Skeletons06
 */
export default function Skeletons06({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="skeletons06" {...props}>
      {children}
    </div>
  )
}