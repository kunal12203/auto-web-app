import { useState } from 'react'

/**
 * DragDropFormBuilder
 * Description: drag and drop form builder
 */
export default function DragDropFormBuilder({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="dragdropformbuilder" {...props}>
      <div className="dragdropformbuilder-content">
        {children}
      </div>
    </div>
  )
}