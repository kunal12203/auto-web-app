import { useState } from 'react'

/**
 * DragDropTreeView
 * Description: draggable tree view
 */
export default function DragDropTreeView({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="dragdroptreeview" {...props}>
      <div className="dragdroptreeview-content">
        {children}
      </div>
    </div>
  )
}