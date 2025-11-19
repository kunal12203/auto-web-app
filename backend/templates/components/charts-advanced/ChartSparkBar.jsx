import { useState } from 'react'

export default function ChartSparkBar({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartsparkbar" {...props}>
      {children}
    </div>
  )
}