import { useState } from 'react'

export default function ChartTreemap3D({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="charttreemap3d" {...props}>
      {children}
    </div>
  )
}