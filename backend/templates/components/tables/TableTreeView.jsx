import { useState } from 'react'

/**
 * TableTreeView
 * Description: tree table with nested rows
 */
export default function TableTreeView({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tabletreeview" {...props}>
      <div className="tabletreeview-content">
        {children}
      </div>
    </div>
  )
}