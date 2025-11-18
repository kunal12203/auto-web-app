import { useState } from 'react'

export default function ChartGrouped({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartgrouped" {...props}>
      {children}
    </div>
  )
}