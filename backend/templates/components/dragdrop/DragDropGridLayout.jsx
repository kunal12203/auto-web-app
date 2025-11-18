import { useState } from 'react'

/**
 * DragDropGridLayout
 * Description: draggable grid layout
 */
export default function DragDropGridLayout({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="dragdropgridlayout" {...props}>
      <div className="dragdropgridlayout-content">
        {children}
      </div>
    </div>
  )
}