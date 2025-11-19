import { useState } from 'react'

export default function ProductPricing({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productpricing" {...props}>
      {children}
    </div>
  )
}