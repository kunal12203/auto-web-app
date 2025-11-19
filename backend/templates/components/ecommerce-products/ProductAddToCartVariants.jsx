import { useState } from 'react'

/**
 * ProductAddToCartVariants
 * Description: add to cart variants
 */
export default function ProductAddToCartVariants({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="productaddtocartvariants" {...props}>
      <div className="productaddtocartvariants-content">
        {children}
      </div>
    </div>
  )
}