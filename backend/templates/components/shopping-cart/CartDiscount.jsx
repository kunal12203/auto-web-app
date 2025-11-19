import { useState } from 'react'

export default function CartDiscount({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="cartdiscount" {...props}>
      {children}
    </div>
  )
}