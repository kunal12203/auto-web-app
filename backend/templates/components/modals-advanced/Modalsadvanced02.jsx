import { useState, useEffect } from 'react'

/**
 * Modalsadvanced02
 */
export default function Modalsadvanced02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="modalsadvanced02" {...props}>
      {children}
    </div>
  )
}