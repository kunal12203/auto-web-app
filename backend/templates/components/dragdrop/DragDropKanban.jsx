import { useState } from 'react'

/**
 * DragDropKanban
 * Description: Kanban board
 */
export default function DragDropKanban({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="dragdropkanban" {...props}>
      <div className="dragdropkanban-content">
        {children}
      </div>
    </div>
  )
}