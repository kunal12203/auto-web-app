import { useState } from 'react'

/**
 * ListDragDrop
 * Description: draggable list items
 */
export default function ListDragDrop({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="listdragdrop" {...props}>
      <div className="listdragdrop-content">
        {children}
      </div>
    </div>
  )
}