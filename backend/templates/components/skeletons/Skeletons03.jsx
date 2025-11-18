import { useState, useEffect } from 'react'

/**
 * Skeletons03
 */
export default function Skeletons03({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="skeletons03" {...props}>
      {children}
    </div>
  )
}