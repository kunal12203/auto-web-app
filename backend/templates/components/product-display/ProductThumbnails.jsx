import { useState } from 'react'

export default function ProductThumbnails({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productthumbnails" {...props}>
      {children}
    </div>
  )
}