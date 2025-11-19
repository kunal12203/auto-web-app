import { useState } from 'react'

/**
 * ListFilterable
 * Description: searchable list
 */
export default function ListFilterable({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="listfilterable" {...props}>
      <div className="listfilterable-content">
        {children}
      </div>
    </div>
  )
}