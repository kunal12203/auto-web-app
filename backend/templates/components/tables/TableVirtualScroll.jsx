import { useState } from 'react'

/**
 * TableVirtualScroll
 * Description: virtualized table for large datasets
 */
export default function TableVirtualScroll({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tablevirtualscroll" {...props}>
      <div className="tablevirtualscroll-content">
        {children}
      </div>
    </div>
  )
}