import { useState } from 'react'

export default function CartSaved({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="cartsaved" {...props}>
      {children}
    </div>
  )
}