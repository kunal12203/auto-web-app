import { useState } from 'react'

/**
 * ProductFiltersAdvanced
 * Description: advanced product filters
 */
export default function ProductFiltersAdvanced({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="productfiltersadvanced" {...props}>
      <div className="productfiltersadvanced-content">
        {children}
      </div>
    </div>
  )
}