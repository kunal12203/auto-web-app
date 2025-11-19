import { useState } from 'react'

export default function ProductVariantSelector({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productvariantselector" {...props}>
      {children}
    </div>
  )
}