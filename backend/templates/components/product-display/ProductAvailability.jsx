import { useState } from 'react'

export default function ProductAvailability({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productavailability" {...props}>
      {children}
    </div>
  )
}