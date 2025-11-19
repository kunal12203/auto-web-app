import { useState, useEffect } from 'react'

/**
 * Tooltipsadvanced02
 */
export default function Tooltipsadvanced02({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tooltipsadvanced02" {...props}>
      {children}
    </div>
  )
}