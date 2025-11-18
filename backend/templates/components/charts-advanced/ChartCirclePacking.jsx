import { useState } from 'react'

export default function ChartCirclePacking({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartcirclepacking" {...props}>
      {children}
    </div>
  )
}