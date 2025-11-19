import { useState, useEffect } from 'react'

/**
 * Cardsadvanced26
 */
export default function Cardsadvanced26({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="cardsadvanced26" {...props}>
      {children}
    </div>
  )
}