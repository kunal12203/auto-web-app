import { useState } from 'react'

export default function CartSummary({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="cartsummary" {...props}>
      {children}
    </div>
  )
}