import { useState } from 'react'

export default function CartItemCard({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="cartitemcard" {...props}>
      {children}
    </div>
  )
}