import { useState } from 'react'

/**
 * GridSortable
 * Description: sortable grid
 */
export default function GridSortable({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="gridsortable" {...props}>
      <div className="gridsortable-content">
        {children}
      </div>
    </div>
  )
}