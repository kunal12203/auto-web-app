import { useState } from 'react'

export default function ChartSparkArea({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartsparkarea" {...props}>
      {children}
    </div>
  )
}