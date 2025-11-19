import { useState } from 'react'

export default function ChartDrilldown({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartdrilldown" {...props}>
      {children}
    </div>
  )
}