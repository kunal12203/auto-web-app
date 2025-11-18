import { useState } from 'react'

export default function CartRecently({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="cartrecently" {...props}>
      {children}
    </div>
  )
}