import { useState } from 'react'

export default function ProductSizeChart({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productsizechart" {...props}>
      {children}
    </div>
  )
}