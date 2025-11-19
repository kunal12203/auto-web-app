import { useState, useEffect } from 'react'

/**
 * Tooltipsadvanced20
 */
export default function Tooltipsadvanced20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tooltipsadvanced20" {...props}>
      {children}
    </div>
  )
}