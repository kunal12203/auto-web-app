import { useState } from 'react'

export default function CartMini({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="cartmini" {...props}>
      {children}
    </div>
  )
}