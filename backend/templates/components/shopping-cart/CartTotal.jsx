import { useState } from 'react'

export default function CartTotal({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="carttotal" {...props}>
      {children}
    </div>
  )
}