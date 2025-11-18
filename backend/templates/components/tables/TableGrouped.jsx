import { useState } from 'react'

/**
 * TableGrouped
 * Description: table with row grouping
 */
export default function TableGrouped({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tablegrouped" {...props}>
      <div className="tablegrouped-content">
        {children}
      </div>
    </div>
  )
}