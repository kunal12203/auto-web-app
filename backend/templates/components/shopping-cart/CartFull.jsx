import { useState } from 'react'

export default function CartFull({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="cartfull" {...props}>
      {children}
    </div>
  )
}