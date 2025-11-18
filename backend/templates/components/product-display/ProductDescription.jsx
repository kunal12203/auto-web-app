import { useState } from 'react'

export default function ProductDescription({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productdescription" {...props}>
      {children}
    </div>
  )
}