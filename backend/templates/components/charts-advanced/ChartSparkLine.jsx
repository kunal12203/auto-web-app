import { useState } from 'react'

export default function ChartSparkLine({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartsparkline" {...props}>
      {children}
    </div>
  )
}