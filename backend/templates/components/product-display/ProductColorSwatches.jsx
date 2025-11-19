import { useState } from 'react'

export default function ProductColorSwatches({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productcolorswatches" {...props}>
      {children}
    </div>
  )
}