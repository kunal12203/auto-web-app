import { useState } from 'react'

export default function ProductZoom({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productzoom" {...props}>
      {children}
    </div>
  )
}