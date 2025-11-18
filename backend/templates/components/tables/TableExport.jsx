import { useState } from 'react'

/**
 * TableExport
 * Description: table with CSV/Excel export
 */
export default function TableExport({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tableexport" {...props}>
      <div className="tableexport-content">
        {children}
      </div>
    </div>
  )
}