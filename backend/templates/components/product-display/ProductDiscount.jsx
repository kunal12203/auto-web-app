import { useState } from 'react'

export default function ProductDiscount({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productdiscount" {...props}>
      {children}
    </div>
  )
}