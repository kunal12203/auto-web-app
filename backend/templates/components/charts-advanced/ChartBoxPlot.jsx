import { useState } from 'react'

export default function ChartBoxPlot({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartboxplot" {...props}>
      {children}
    </div>
  )
}