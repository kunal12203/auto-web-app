import { useState } from 'react'

export default function ChartMesh({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartmesh" {...props}>
      {children}
    </div>
  )
}