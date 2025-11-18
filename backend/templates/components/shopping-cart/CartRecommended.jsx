import { useState } from 'react'

export default function CartRecommended({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="cartrecommended" {...props}>
      {children}
    </div>
  )
}