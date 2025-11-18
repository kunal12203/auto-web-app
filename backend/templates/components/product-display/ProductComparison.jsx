import { useState } from 'react'

export default function ProductComparison({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productcomparison" {...props}>
      {children}
    </div>
  )
}