import { useState } from 'react'

/**
 * TableFrozenColumns
 * Description: table with frozen columns
 */
export default function TableFrozenColumns({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tablefrozencolumns" {...props}>
      <div className="tablefrozencolumns-content">
        {children}
      </div>
    </div>
  )
}