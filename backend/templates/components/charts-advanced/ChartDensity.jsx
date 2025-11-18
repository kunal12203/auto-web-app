import { useState } from 'react'

export default function ChartDensity({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartdensity" {...props}>
      {children}
    </div>
  )
}