import { useState } from 'react'

/**
 * ProductCardVariantA
 * Description: product card variant A
 */
export default function ProductCardVariantA({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="productcardvarianta" {...props}>
      <div className="productcardvarianta-content">
        {children}
      </div>
    </div>
  )
}