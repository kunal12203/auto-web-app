import { useState } from 'react'

/**
 * ProductListView
 * Description: product list view
 */
export default function ProductListView({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="productlistview" {...props}>
      <div className="productlistview-content">
        {children}
      </div>
    </div>
  )
}