import { useState } from 'react'

export default function Chart3D({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chart3d" {...props}>
      {children}
    </div>
  )
}