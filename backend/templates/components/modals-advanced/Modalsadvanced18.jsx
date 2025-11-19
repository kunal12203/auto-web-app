import { useState, useEffect } from 'react'

/**
 * Modalsadvanced18
 */
export default function Modalsadvanced18({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="modalsadvanced18" {...props}>
      {children}
    </div>
  )
}