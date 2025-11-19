import { useState } from 'react'

export default function ProductRating({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productrating" {...props}>
      {children}
    </div>
  )
}