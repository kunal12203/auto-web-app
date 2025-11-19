import { useState } from 'react'

export default function CartEmpty({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="cartempty" {...props}>
      {children}
    </div>
  )
}