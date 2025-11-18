import { useState } from 'react'

export default function CartDrawer({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="cartdrawer" {...props}>
      {children}
    </div>
  )
}