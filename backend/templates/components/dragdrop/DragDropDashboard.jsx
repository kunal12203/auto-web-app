import { useState } from 'react'

/**
 * DragDropDashboard
 * Description: draggable dashboard widgets
 */
export default function DragDropDashboard({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="dragdropdashboard" {...props}>
      <div className="dragdropdashboard-content">
        {children}
      </div>
    </div>
  )
}