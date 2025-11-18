import { useState } from 'react'

/**
 * TableDragDrop
 * Description: table with draggable rows
 */
export default function TableDragDrop({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tabledragdrop" {...props}>
      <div className="tabledragdrop-content">
        {children}
      </div>
    </div>
  )
}