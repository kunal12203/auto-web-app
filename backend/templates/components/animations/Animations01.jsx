import { useState, useEffect } from 'react'

/**
 * Animations01
 */
export default function Animations01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="animations01" {...props}>
      {children}
    </div>
  )
}