import { useState } from 'react'

export default function ProductRelated({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productrelated" {...props}>
      {children}
    </div>
  )
}