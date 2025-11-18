import { useState } from 'react'

export default function ProductShipping({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productshipping" {...props}>
      {children}
    </div>
  )
}