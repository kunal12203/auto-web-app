import { useState } from 'react'

export default function ChartPointFigure({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartpointfigure" {...props}>
      {children}
    </div>
  )
}