import { useState } from 'react'

/**
 * ProductCompare
 * Description: product comparison
 */
export default function ProductCompare({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="productcompare" {...props}>
      <div className="productcompare-content">
        {children}
      </div>
    </div>
  )
}