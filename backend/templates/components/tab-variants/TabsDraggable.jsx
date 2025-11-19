import { useState } from 'react'

/**
 * TabsDraggable
 * Description: draggable tabs
 */
export default function TabsDraggable({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tabsdraggable" {...props}>
      <div className="tabsdraggable-content">
        {children}
      </div>
    </div>
  )
}