import { useState } from 'react'

export default function ProductStock({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productstock" {...props}>
      {children}
    </div>
  )
}