import { useState } from 'react'

/**
 * GridDragDrop
 * Description: draggable grid items
 */
export default function GridDragDrop({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="griddragdrop" {...props}>
      <div className="griddragdrop-content">
        {children}
      </div>
    </div>
  )
}