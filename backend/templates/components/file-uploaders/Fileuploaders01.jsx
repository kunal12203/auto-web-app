import { useState, useEffect } from 'react'

/**
 * Fileuploaders01
 */
export default function Fileuploaders01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders01" {...props}>
      {children}
    </div>
  )
}