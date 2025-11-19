import { useState } from 'react'

/**
 * ListGrouped
 * Description: list with group headers
 */
export default function ListGrouped({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="listgrouped" {...props}>
      <div className="listgrouped-content">
        {children}
      </div>
    </div>
  )
}