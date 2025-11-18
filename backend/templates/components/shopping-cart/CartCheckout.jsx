import { useState } from 'react'

export default function CartCheckout({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="cartcheckout" {...props}>
      {children}
    </div>
  )
}