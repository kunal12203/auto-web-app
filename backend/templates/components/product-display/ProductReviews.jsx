import { useState } from 'react'

export default function ProductReviews({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productreviews" {...props}>
      {children}
    </div>
  )
}