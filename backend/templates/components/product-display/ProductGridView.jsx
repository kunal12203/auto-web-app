import { useState } from 'react'

export default function ProductGridView({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productgridview" {...props}>
      {children}
    </div>
  )
}