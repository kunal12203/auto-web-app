import { useState } from 'react'

/**
 * TableExpandable
 * Description: table with expandable rows
 */
export default function TableExpandable({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tableexpandable" {...props}>
      <div className="tableexpandable-content">
        {children}
      </div>
    </div>
  )
}