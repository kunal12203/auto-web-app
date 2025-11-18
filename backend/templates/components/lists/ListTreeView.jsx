import { useState } from 'react'

/**
 * ListTreeView
 * Description: tree view list
 */
export default function ListTreeView({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="listtreeview" {...props}>
      <div className="listtreeview-content">
        {children}
      </div>
    </div>
  )
}