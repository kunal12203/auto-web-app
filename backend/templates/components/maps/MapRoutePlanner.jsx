import { useState } from 'react'

/**
 * MapRoutePlanner
 * Description: route planning map
 */
export default function MapRoutePlanner({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="maprouteplanner" {...props}>
      <div className="maprouteplanner-content">
        {children}
      </div>
    </div>
  )
}