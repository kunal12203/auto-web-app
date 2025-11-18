import { useState } from 'react'

export default function ProductWarranty({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productwarranty" {...props}>
      {children}
    </div>
  )
}