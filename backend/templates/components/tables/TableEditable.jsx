import { useState } from 'react'

/**
 * TableEditable
 * Description: editable table cells
 */
export default function TableEditable({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tableeditable" {...props}>
      <div className="tableeditable-content">
        {children}
      </div>
    </div>
  )
}