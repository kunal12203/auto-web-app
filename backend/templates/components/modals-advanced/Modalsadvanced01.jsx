import { useState, useEffect } from 'react'

/**
 * Modalsadvanced01
 */
export default function Modalsadvanced01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="modalsadvanced01" {...props}>
      {children}
    </div>
  )
}