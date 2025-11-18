import { useState, useEffect } from 'react'

/**
 * Tooltipsadvanced01
 */
export default function Tooltipsadvanced01({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="tooltipsadvanced01" {...props}>
      {children}
    </div>
  )
}