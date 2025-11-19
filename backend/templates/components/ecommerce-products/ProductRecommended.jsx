import { useState } from 'react'

/**
 * ProductRecommended
 * Description: recommended products
 */
export default function ProductRecommended({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="productrecommended" {...props}>
      <div className="productrecommended-content">
        {children}
      </div>
    </div>
  )
}