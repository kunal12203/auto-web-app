import { useState } from 'react'

export default function CartSidebar({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="cartsidebar" {...props}>
      {children}
    </div>
  )
}