import { useState } from 'react'

/**
 * ProductSizeSelector
 * Description: size selector
 */
export default function ProductSizeSelector({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="productsizeselector" {...props}>
      <div className="productsizeselector-content">
        {children}
      </div>
    </div>
  )
}