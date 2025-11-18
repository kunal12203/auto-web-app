import { useState } from 'react'

export default function ProductReturns({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productreturns" {...props}>
      {children}
    </div>
  )
}