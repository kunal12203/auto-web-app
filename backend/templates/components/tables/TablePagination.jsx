import { useState } from 'react'

/**
 * TablePagination
 * Description: table with pagination controls
 */
export default function TablePagination({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tablepagination" {...props}>
      <div className="tablepagination-content">
        {children}
      </div>
    </div>
  )
}