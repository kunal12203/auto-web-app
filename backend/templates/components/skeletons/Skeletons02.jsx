import { useState, useEffect } from 'react'

/**
 * Skeletons02
 */
export default function Skeletons02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="skeletons02" {...props}>
      {children}
    </div>
  )
}