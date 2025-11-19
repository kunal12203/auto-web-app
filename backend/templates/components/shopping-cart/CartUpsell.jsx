import { useState } from 'react'

export default function CartUpsell({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="cartupsell" {...props}>
      {children}
    </div>
  )
}