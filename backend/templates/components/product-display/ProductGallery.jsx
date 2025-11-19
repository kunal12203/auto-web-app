import { useState } from 'react'

export default function ProductGallery({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productgallery" {...props}>
      {children}
    </div>
  )
}