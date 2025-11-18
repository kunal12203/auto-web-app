import { useState } from 'react'

/**
 * TableSortable
 * Description: sortable table with column sorting
 */
export default function TableSortable({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tablesortable" {...props}>
      <div className="tablesortable-content">
        {children}
      </div>
    </div>
  )
}