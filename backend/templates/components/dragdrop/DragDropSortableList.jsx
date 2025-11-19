import { useState } from 'react'

/**
 * DragDropSortableList
 * Description: sortable list with drag
 */
export default function DragDropSortableList({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="dragdropsortablelist" {...props}>
      <div className="dragdropsortablelist-content">
        {children}
      </div>
    </div>
  )
}