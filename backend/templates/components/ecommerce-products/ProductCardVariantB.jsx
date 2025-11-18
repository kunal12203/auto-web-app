import { useState } from 'react'

/**
 * ProductCardVariantB
 * Description: product card variant B
 */
export default function ProductCardVariantB({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="productcardvariantb" {...props}>
      <div className="productcardvariantb-content">
        {children}
      </div>
    </div>
  )
}