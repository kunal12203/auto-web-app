import { useState } from 'react'

/**
 * TableFilterable
 * Description: filterable table with search
 */
export default function TableFilterable({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tablefilterable" {...props}>
      <div className="tablefilterable-content">
        {children}
      </div>
    </div>
  )
}