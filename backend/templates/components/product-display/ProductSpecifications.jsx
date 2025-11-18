import { useState } from 'react'

export default function ProductSpecifications({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productspecifications" {...props}>
      {children}
    </div>
  )
}