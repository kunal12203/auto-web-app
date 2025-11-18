import { useState } from 'react'

/**
 * ListAnimated
 * Description: animated list transitions
 */
export default function ListAnimated({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="listanimated" {...props}>
      <div className="listanimated-content">
        {children}
      </div>
    </div>
  )
}