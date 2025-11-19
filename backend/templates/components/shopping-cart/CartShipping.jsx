import { useState } from 'react'

export default function CartShipping({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="cartshipping" {...props}>
      {children}
    </div>
  )
}