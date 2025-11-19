import { useState } from 'react'

export default function ProductCarousel({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productcarousel" {...props}>
      {children}
    </div>
  )
}