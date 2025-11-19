import { useState } from 'react'

export default function ChartSurface({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartsurface" {...props}>
      {children}
    </div>
  )
}