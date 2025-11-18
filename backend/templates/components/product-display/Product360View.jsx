import { useState } from 'react'

export default function Product360View({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="product360view" {...props}>
      {children}
    </div>
  )
}