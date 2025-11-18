import { useState, useEffect } from 'react'

/**
 * Fileuploaders20
 */
export default function Fileuploaders20({ children, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Component logic
  }, [])

  return (
    <div className="fileuploaders20" {...props}>
      {children}
    </div>
  )
}