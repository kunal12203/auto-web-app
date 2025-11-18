import { useState, useEffect } from 'react'

/**
 * Modalsadvanced20
 */
export default function Modalsadvanced20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="modalsadvanced20" {...props}>
      {children}
    </div>
  )
}