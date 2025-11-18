import { useState, useEffect } from 'react'

/**
 * Tooltipsadvanced18
 */
export default function Tooltipsadvanced18({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tooltipsadvanced18" {...props}>
      {children}
    </div>
  )
}