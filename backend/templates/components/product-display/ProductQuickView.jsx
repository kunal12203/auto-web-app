import { useState } from 'react'

export default function ProductQuickView({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productquickview" {...props}>
      {children}
    </div>
  )
}